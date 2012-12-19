import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

from gwhiz.model import meta
from gwhiz import model
from webhelpers.textile import textile
class ArtistController(BaseController):

    def view(self,id):
        c.artist = meta.Session.query(model.Artist).get(id)
        if c.artist.bio:
            c.bio = textile(c.artist.bio)
        #meta.Session.query(model.Album).filter(model.Album.artists.contains(c.artist)).all()
        #c.numworks = len(q.all())
        #c.featured = q.filter_by(featured=True).all()
        return render('/artist/detail.html')
