import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn

from pylons import h

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/auth.mako')
        # or, return a response
        if 'GWHIZ' in session:
            session['GWHIZ'] += 1
            session.save()
            return ('gwhizfound', session['GWHIZ'])
        else:
            session['GWHIZ'] = 1
            session.save()
            return '<p>'.join(session)


    @authorize(ValidAuthKitUser())
    #@authorize(UserIn(["visitor"]))
    def private(self):
        return "You are authenticated! " + h.link_to('signout','/auth/signout')


    def private_manual(self):
        if request.environ.get("REMOTE_USER"):
            return "You are authenticated!"
        else:
            response.status = "401 Not authenticated"
            return "You are not authenticated"

    def signout(self):
        return "Successfully signed out!"
