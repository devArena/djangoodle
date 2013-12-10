

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Taken from http://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys
try:
    from secret_key import *
except ImportError:
    SETTINGS_DIR=os.path.abspath(os.path.dirname(__file__))
    def generate_secret_key(file_name):
        import string
        from django.utils.crypto import get_random_string
        f = open(file_name, 'w')
        key = 'SECRET_KEY = "{}"\n'.format(get_random_string(100, string.ascii_letters))
        f.write(key)
        f.close()
    generate_secret_key(os.path.join(SETTINGS_DIR, 'secret_key.py'))
    from secret_key import *

try:
    from settings_secret import *
except ImportError:
    print('ERROR: Secret settings not loaded!')

