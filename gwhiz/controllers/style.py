import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

from gwhiz.model import meta
from gwhiz import model

log = logging.getLogger(__name__)

class StyleController(BaseController):

    def list(self,id):
        style = meta.Session.query(model.Style).get(id)
        works = meta.Session.query(model.Work)
        c.cat = style
        c.works = works.filter(model.Work.styles.contains(style)).order_by(model.Work.title)
        c.info = 'Viewing Publications with Style: %s'%style.name

        c.publications = meta.Session.query(model.Publication).filter(model.Publication.styles.contains(style)).order_by(model.Publication.catalog_number)

        return render('/catalog/list.html')
