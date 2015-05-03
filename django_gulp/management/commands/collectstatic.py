import os
import subprocess

from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as BaseCommand


class Command(BaseCommand):
    """
    A version of collectstatic that runs `gulp build --production` first.
    """
    def handle(self, *args, **options):
        if options['dry_run']:
            return

        popen_args = {
            'shell': True,
            'stdin': subprocess.PIPE,
            'stdout': self.stdout,
            'stderr': self.stderr
        }

        # HACK: This command is executed without node_modules in the PATH
        # when it's executed from Heroku... Ideally we wouldn't need any
        # Heroku-specific code for this to work.
        if os.path.exists('/app/requirements.txt'):
            popen_args['env'] = {
                'PATH': (os.environ['PATH'] +
                         ':/app/node_modules/.bin' +
                         ':/app/.heroku/node/bin')
            }

        subprocess.Popen(['gulp build --production'],
                         **popen_args).wait()

        super(Command, self).handle(*args, **options)
