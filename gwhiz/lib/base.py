"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons import request, response, session, tmpl_context as c
from gwhiz.model import meta
from gwhiz import model

from pylons.controllers import WSGIController
from pylons.templating import render_mako as render

from gwhiz.model import meta
import gwhiz

import logging
log = logging.getLogger(__name__)




class BaseController(WSGIController):
    cname = 'GWHIZ'
    #sections = 'Home,News,Composers,Catalog,Services,Media,Friends,Contact'.split(',')
    sections = [['Home',None],
                ['Bios','Composer Biographies'],
                ['Catalog','Music Catalog'],
                ['Services','Services'],
                ['Friends','Friends'],
                ['Contact','Contact']]
    subsections = {}
    def __before__(self):
        c.cart = self.parse_cart_cookie()
        c.current_section = request.environ['pylons.routes_dict']['controller']
        c.sections = self.sections
        c.subsections = self.subsections
        c.controllerfile = '/home/kgraehl/gwhiz/controllers/'+c.current_section+'.py'

        try:
            i = [k for k,v in self.sections].index(c.current_section.capitalize())
            c.current_sectiontitle = self.sections[i][1]
        except:
            if c.current_section in ['style','composer','instrument','key']:
                c.current_section = 'catalog'
                c.current_sectiontitle = 'Music Catalog'
                c.subsections = {'View by Instrument':'by_instrument',\
                'View by Composer':'by_composer',\
                'View by Style':'by_style',\
                'View by Key':'by_key',}

            else:
                c.current_sectiontitle = None
        import random
        import os

    def parse_cart_cookie(self):
        toreturn = []
        if self.cname in session:
	    log.info('self.cname %s' %self.cname)
            items = session[self.cname].split(',')
	    """log.info('Items %s' %items)"""
            for item in items:
                if item:
		    """log.info('Item %s' %item)"""
		    type = None
                    type,id = item.split('-')
		    """log.info('Type %s' %type)"""
                    if type in ['Publication']:
                        obj = meta.Session.query(getattr(model,type)).get(id)
                        toreturn.append(obj)
        return toreturn

    def save_cart_cookie(self):
        if self.cname in session:
            tosave = ','.join(['%s-%s'%(obj.__class__.__name__, obj.id) for obj in c.cart])
            session[self.cname] = tosave
            session.save()


    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()
