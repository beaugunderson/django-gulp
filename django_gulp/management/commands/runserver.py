import sys

from colors import color

from django.contrib.staticfiles.management.commands.runserver import (
    Command as StaticfilesRunserverCommand)
from django.core.servers import basehttp

from .runserver_mixin import RunserverMixin


@staticmethod
def log_local_message(message_format, *args):
    """
    Log a request so that it matches our local log format.
    """
    prefix = '{} {}'.format(color('INFO', fg=248), color('request', fg=5))
    message = message_format % args

    sys.stderr.write('{} {}\n'.format(prefix, message))

basehttp.WSGIRequestHandler.log_message = log_local_message


class Command(RunserverMixin, StaticfilesRunserverCommand):
    """
    Subclass the RunserverCommand from Staticfiles to set up our gulp
    environment.
    """

    pass
