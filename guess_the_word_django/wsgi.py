import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guess_the_word_django.settings')

application = get_wsgi_application()
