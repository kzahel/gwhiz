import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

from gwhiz.model import meta
from gwhiz import model

class InstrumentController(BaseController):
    subsections = {}
    def index(self):
        # Return a rendered template
        #return render('/instrument.mako')
        # or, return a response
        return 'Hello World'

    def list(self,id):
        instrument = meta.Session.query(model.Instrument).get(id)
        publications = meta.Session.query(model.Publication)
        c.cat = instrument
        c.publications = publications.filter(model.Publication.instruments.contains(instrument)).all()
        c.info = 'Viewing Publications with Instrument: %s'%instrument.name
        return render('/catalog/list.html')
