from .base import *

SECRET_KEY = env("DJANGO_SECRET_KEY", default="'django-insecure-m0lzhm@x_w7pc$d!*wlkdw4=tf%75_!_6&=-8cm@bq&tfi@1qb'")
DEBUG = env.bool("DJANGO_DEBUG", default=True)