from .base import *


# removing security enforcement in development mode
DEBUG = True
SECRET_KEY = env('DJANGO_SECRET_KEY', '1234567890')

# enabling console loggers
LOGGING['loggers'] = {
    'django': {
        'handlers': ['console'],
        'level': env('DJANGO_LOG_LEVEL', 'INFO'),
    },
    '{{ cookiecutter.app_name }}': {
        'handlers': ['console'],
        'level': env('{{ cookiecutter.app_name|upper }}_LOG_LEVEL', 'DEBUG'),
    },
}
