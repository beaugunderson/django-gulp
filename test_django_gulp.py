from django.conf import settings

if not settings.configured:
    settings.configure(
        MIGRATION_MODULES={'__main__': 'migrations'},
        INSTALLED_APPS=('__main__',))

from django.apps import apps

apps.populate(settings.INSTALLED_APPS)


# pylint: disable=unused-variable
def test_does_not_explode():
    """
    The module should import without error.
    """
    from django_gulp.management.commands import collectstatic   # noqa
    from django_gulp.management.commands import runserver       # noqa
    from django_gulp.management.commands import runserver_plus  # noqa
