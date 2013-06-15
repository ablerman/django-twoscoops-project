from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand
from django.utils.importlib import import_module
from django.conf import settings

class Command(TemplateCommand):
    help = ("Creates a Django app directory structure for the given app "
            "name in the current directory or optionally in the given "
            "directory.")

    def handle(self, app_name=None, target=None, **options):
        if app_name is None:
            raise CommandError("you must provide an app name")

        # Check that the app_name cannot be imported.
        try:
            import_module(app_name)
        except ImportError:
            pass
        else:
            raise CommandError("%r conflicts with the name of an existing "
                               "Python module and cannot be used as an app "
                               "name. Please try another name." % app_name)

        if ('template' not in options or options['template'] is None ) and hasattr(settings, 'DEFAULT_APP_TEMPLATE'):
            options['template'] = settings.DEFAULT_APP_TEMPLATE

        # print options
        # return
        super(Command, self).handle('app', app_name, target, **options)
