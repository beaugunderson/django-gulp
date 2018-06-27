from django_extensions.management.commands.runserver_plus import (
    Command as DjangoExtensionsRunserverCommand)

from .runserver_mixin import RunserverMixin


class Command(RunserverMixin, DjangoExtensionsRunserverCommand):
    """
    Subclass the DjangoExtensionsRunserverCommand from django-extensions to set
    up our gulp environment.
    """

    pass
