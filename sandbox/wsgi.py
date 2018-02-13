# isort:skip
import os
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application  # isort:skip


application = get_wsgi_application()
application = DjangoWhiteNoise(application)