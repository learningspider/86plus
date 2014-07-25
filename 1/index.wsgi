import sae
from 86plus import wsgi
 
application = sae.create_wsgi_app(wsgi.application)

