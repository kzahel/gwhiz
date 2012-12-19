import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

class EmacsclientController(BaseController):

    def index(self,id):
        import os
        id = id.replace('@','/')
        #os.system('emacsclient -n %s'%id)
        return id

        # Return a rendered template
        #return render('/emacsclient.mako')
        # or, return a response

