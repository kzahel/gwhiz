import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

from gwhiz import model
from gwhiz.model import meta
from webhelpers.textile import textile

class BiosController(BaseController):

    def index(self):
        c.composers = meta.Session.query(model.Composer).all()
        return render('/bios/list.html')

    def view(self,id):
        c.composer = meta.Session.query(model.Composer).get(id)
        c.bio = textile(c.composer.bio)
        c.numworks = len(c.composer.works)
        c.numpublications = len(c.composer.publications)
        c.featured_works = [w for w in c.composer.works if w.featured == True]
        c.featured_publications = [w for w in c.composer.publications if w.featured == True]
        return render('/bios/detail.html')
