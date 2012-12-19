import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

from gwhiz.model import meta
from gwhiz import model

class ComposerController(BaseController):

    def list(self,id):
        composer = meta.Session.query(model.Composer).get(id)
        c.composer = composer
        #works = meta.Session.query(model.Work)
        #c.works = works.filter_by(composer=composer).order_by(model.Work.title).all()
        #c.works = works.filter_by(composer=composer).all()
        #c.movements = works.filter_by(composer=composer).all()
        from sqlalchemy import or_, and_, desc, asc
        c.publications = meta.Session.query(model.Publication).filter(model.Publication.composers.contains(composer)).order_by(model.Publication.catalog_number)
        return render('/catalog/composerlist.html')

##     def publications(self,id):
##         composer = meta.Session.query(model.Composer).get(id)
##         c.composer = composer
##         c.publications = meta.Session.query(model.Publication).filter(model.Publication.composers.contains(composer)).order_by(model.Publication.title).all()
##         print c.publications
##         return render('/catalog/publicationlist.html')

