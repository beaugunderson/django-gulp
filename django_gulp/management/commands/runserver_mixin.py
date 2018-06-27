from __future__ import print_function

import atexit
import os
import psutil
import subprocess
import sys
import traceback

from signal import SIGTERM

from concurrent.futures import ThreadPoolExecutor

from colors import color

from django.core.management.base import CommandError
from django.conf import settings

from env_tools import load_env


class RunserverMixin(object):
    """
    Subclass the DjangoExtensionsRunserverCommand from django-extensions to set
    up our gulp environment.
    """

    pass

    def __init__(self, *args, **kwargs):
        self.cleanup_closing = False
        self.gulp_process = None

        super(RunserverMixin, self).__init__(*args, **kwargs)

    @staticmethod
    def gulp_exited_cb(future):
        if future.exception():
            print(traceback.format_exc())

            children = psutil.Process().children(recursive=True)

            for child in children:
                print('>>> Killing pid {}'.format(child.pid))

                child.send_signal(SIGTERM)

            print('>>> Exiting')

            # It would be nice to be able to raise a CommandError or use
            # sys.kill here but neither of those stop the runserver instance
            # since we're in a thread. This method is used in django as well.
            os._exit(1)

    def handle(self, *args, **options):
        try:
            env = load_env()
        except IOError:
            env = {}

        # XXX: In Django 1.8 this changes to:
        # if 'PORT' in env and not options.get('addrport'):
        #     options['addrport'] = env['PORT']

        if 'PORT' in env and not args:
            args = (env['PORT'],)

        # We're subclassing runserver, which spawns threads for its
        # autoreloader with RUN_MAIN set to true, we have to check for
        # this to avoid running gulp twice.
        if not os.getenv('RUN_MAIN', False):
            pool = ThreadPoolExecutor(max_workers=1)

            gulp_thread = pool.submit(self.start_gulp)
            gulp_thread.add_done_callback(self.gulp_exited_cb)

        return super(RunserverMixin, self).handle(*args, **options)

    def kill_gulp_process(self):
        if self.gulp_process.returncode is not None:
            return

        self.cleanup_closing = True
        self.stdout.write('>>> Closing gulp process')

        self.gulp_process.terminate()

    def start_gulp(self):
        self.stdout.write('>>> Starting gulp')

        gulp_cwd = getattr(settings, 'GULP_CWD', os.getcwd())

        gulp_command = getattr(settings,
                               'GULP_DEVELOP_COMMAND',
                               'gulp --cwd %s' % gulp_cwd)

        self.gulp_process = subprocess.Popen(
            gulp_command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout._out,
            stderr=self.stderr._out)

        if self.gulp_process.poll() is not None:
            raise CommandError('gulp failed to start')

        self.stdout.write('>>> gulp process on pid {0}'
                          .format(self.gulp_process.pid))

        atexit.register(self.kill_gulp_process)

        self.gulp_process.wait()

        if self.gulp_process.returncode != 0 and not self.cleanup_closing:
            raise CommandError('gulp exited unexpectedly')
