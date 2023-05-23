from .settings import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ["goldenline-project.herokuapp.com"]

SECRET_KEY = "toa5+@)s8@(dyn7m5^m#p8rglrk@d)c09+p(d6u9wepzg8a57%"

DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)
