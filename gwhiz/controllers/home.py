import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render
from gwhiz.model import meta
from gwhiz import model

log = logging.getLogger(__name__)
from sqlalchemy import desc

class HomeController(BaseController):

    def index(self):
        c.featuredpublications = meta.Session.query(model.Publication).filter_by(featured=True).order_by(desc(model.Publication.id)).all()
        return render('/home/base.html')
