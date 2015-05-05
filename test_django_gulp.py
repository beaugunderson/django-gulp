# pylint: disable=unused-variable
def test_does_not_explode():
    """
    The module should import without error.
    """
    from django.conf import settings

    settings.configure()

    from django_gulp.management.commands import collectstatic  # noqa
    from django_gulp.management.commands import runserver      # noqa
