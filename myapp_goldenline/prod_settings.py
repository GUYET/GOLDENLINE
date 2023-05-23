from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False
LLOWED_HOSTS = ["goldenline-project.herokuapp.com"]


DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)
