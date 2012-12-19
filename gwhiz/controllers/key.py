import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

from gwhiz.model import meta
from gwhiz import model


class KeyController(BaseController):

    def list(self,id):
        key = meta.Session.query(model.Key).get(id)
        c.cat = key
        c.works = meta.Session.query(model.Work).filter_by(key=key)
        c.movements = meta.Session.query(model.Movement).filter_by(key=key)
        #c.works = works.filter(model.Work.key.contains(style)).all()
        c.info = 'Viewing by Key: %s'%key.name

        return render('/catalog/combinedlist.html')
