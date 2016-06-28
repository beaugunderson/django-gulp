import os
import subprocess

from django.conf import settings
from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as BaseCommand
from django.core.management.base import CommandError


class Command(BaseCommand):
    """
    A version of collectstatic that runs `gulp build --production` first.
    """

    def handle(self, *args, **options):
        if options['dry_run']:
            return

        popen_kwargs = {
            'shell': True,
            'stdin': subprocess.PIPE,
            'stdout': self.stdout,
            'stderr': self.stderr
        }

        # HACK: This command is executed without node_modules in the PATH
        # when it's executed from Heroku... Ideally we wouldn't need any
        # Heroku-specific code for this to work.
        if os.path.exists('/app/requirements.txt'):
            popen_kwargs['env'] = {
                'PATH': (os.environ['PATH'] +
                         ':/app/node_modules/.bin' +
                         ':/app/.heroku/node/bin')
            }

        gulp_command = getattr(
            settings, 'GULP_PRODUCTION_COMMAND', 'gulp build --production')
        try:
            subprocess.check_call(gulp_command, **popen_kwargs)
        except subprocess.CalledProcessError as e:
            raise CommandError(e)

        super(Command, self).handle(*args, **options)
