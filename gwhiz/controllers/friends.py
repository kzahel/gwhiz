import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

class FriendsController(BaseController):

    def index(self):
        return render('/friends/base.html')
