import sae
from wsucai import wsgi
 
application = sae.create_wsgi_app(wsgi.application)

