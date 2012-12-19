import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

class NavController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/nav.mako')
        # or, return a response
        return 'Hello World'