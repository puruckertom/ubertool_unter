import os
import sys

if __name__ == "__main__":

    if os.path.abspath(__file__) == os.path.join('/', 'var', 'www', 'ubertool', 'ubertool_unter', 'manage.py'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_apache")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_apache")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
