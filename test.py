# settings.py
from django.conf import settings

settings.configure(
    DATABASES = {
            'default': {
                        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
                        'USER': '',                      # Not used with sqlite3.
                        'PASSWORD': '',                  # Not used with sqlite3.
                        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
                        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
                    }
    },
        INSTALLED_APPS     = ("")
)

from myblog.models import Blog
blogs = Blog.objects.all()[0].title
print blogs
