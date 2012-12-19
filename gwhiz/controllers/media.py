import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

from gwhiz.model import meta
from gwhiz import model

log = logging.getLogger(__name__)

class MediaController(BaseController):

    def index(self):
        return render('/media/base.html')

    def music(self):
        c.soundclips = meta.Session.query(model.Soundclip).all()
        return render('/media/music.html')

    def video(self):
        return render('/media/video.html')
