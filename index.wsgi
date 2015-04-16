import sae

from mysite02 import wsgi

application = sae.create_wsgi_app(wsgi.application)