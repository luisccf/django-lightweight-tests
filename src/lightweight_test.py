import logging
import sys
import warnings
from abc import ABC, abstractmethod

from django import VERSION as DJANGO_VERSION
from django.conf import settings


class LightweightTestOption(ABC):
    @property
    @abstractmethod
    def msg(self):
        pass


class NoMigrations(LightweightTestOption):
    msg = 'Disabling migrations'

    class FakeMigrationsModule:
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    def __init__(self):
        settings.MIGRATION_MODULES = NoMigrations.FakeMigrationsModule()


class NoWarnings(LightweightTestOption):
    msg = 'Disabling warnings'

    def __init__(self):
        logging.disable(logging.CRITICAL)
        warnings.filterwarnings('ignore', category=RuntimeWarning)


class DebugFalse(LightweightTestOption):
    msg = 'Setting DEBUG False'

    def __init__(self):
        settings.DEBUG = False
        settings.TEMPLATE_DEBUG = False


class SimpleHash(LightweightTestOption):
    msg = 'Setting password hasher to md5'

    def __init__(self):
        settings.PASSWORD_HASHERS = [
            'django.contrib.auth.hashers.MD5PasswordHasher',
        ]


class SimpleMiddlewares(LightweightTestOption):
    msg = 'Setting necessary middleware classes only'

    def __init__(self):
        settings.MIDDLEWARE_CLASSES = [
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ]


class SQLite(LightweightTestOption):
    msg = 'Changing db to SQLite'

    def __init__(self):
        settings.DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test_database',
            }
        }


class LightweightTest:
    option_classes = [
        NoWarnings,
        DebugFalse,
        SimpleHash,
        SimpleMiddlewares,
        SQLite,
        NoMigrations,
    ]

    def __init__(self, cmd_option='--light', verbosity=0):
        self.cmd_option = cmd_option
        self.verbosity = verbosity

        for option_class in self.option_classes:
            self.add_option(option_class)

        try:
            sys.argv.remove(self.cmd_option)
        except ValueError:
            pass

    def add_option(self, option_class):
        option = option_class()
        if self.verbosity > 0:
            print(option.msg)
