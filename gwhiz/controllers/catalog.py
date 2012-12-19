import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

from gwhiz.model import meta
from gwhiz import model
from webhelpers.textile import textile

class CatalogController(BaseController):

    subsections = {'View by Instrument':'by_instrument',\
                'View by Composer':'by_composer',\
                'View by Style':'by_style',\
                'View by Key':'by_key',}
    #subsections = {'View by Composer':'by_composer'}

    def index(self):
        c.feature = 'Ring Tones'
        redirect_to(controller='catalog',action='by_composer')
        #return render('/catalog/base.html')

    def by_composer(self):
        q = meta.Session.query(model.Composer)
        c.categories = q.all()
        c.type = 'Composer'
        c.controller = 'composer'

        works = meta.Session.query(model.Work)
        publications = meta.Session.query(model.Publication)
        c.numincat = []
        for n,composer in enumerate(c.categories):
            c.numincat.append( publications.filter(model.Publication.composers.contains(composer)).count() )

        return render('/catalog/category.html')

    def by_key(self):
        q = meta.Session.query(model.Key)
        c.categories = q.order_by(model.Key.name)
        c.type = 'Key'
        c.controller = 'key'

        works = meta.Session.query(model.Work)
        movements = meta.Session.query(model.Movement)
        c.numincat = []
        for n,key in enumerate(c.categories):
            c.numincat.append( len( works.filter_by(key=key).all() ) + len( movements.filter_by(key=key).all() ) )

        return render('/catalog/category.html')


    def by_style(self):
        c.categories = meta.Session.query(model.Style).order_by(model.Style.name)
        c.type = 'Style'
        c.controller = 'style'

        publications = meta.Session.query(model.Publication)
        c.numincat = []
        for n,style in enumerate(c.categories):
            c.numincat.append( publications.filter(model.Publication.styles.contains(style)).count() )
            #c.numincat.append( n )

        return render('/catalog/category.html')

    def by_instrument(self):
        q = meta.Session.query(model.Instrument)
        c.categories = q.order_by(model.Instrument.name)
        c.type = 'Instrument'
        c.controller = 'instrument'

        works = meta.Session.query(model.Work)
        c.numincat = []
        for n,instrument in enumerate(c.categories):
            c.numincat.append( len( works.filter(model.Work.instruments.contains(instrument)).all() ) )
            #c.numincat.append( n )

        return render('/catalog/category.html')

    def workdetail(self,id):
        q = meta.Session.query(model.Work).get(id)
        c.work = q
        if c.work.description:
            c.work.description = textile(c.work.description)
        return render('/catalog/workdetail.html')

    def publicationdetail(self,id):
        c.publication = meta.Session.query(model.Publication).get(id)
        if c.publication.description:
            c.publication.description = textile(c.publication.description)
        return render('/catalog/publicationdetail.html')


    def movementdetail(self,id):
        q = meta.Session.query(model.Movement).get(id)
        c.movement = q
        return render('/catalog/movementdetail.html')

    def addtocart(self,id):
        type,id = id.split('-')
        if self.cname in session:
            session[self.cname] = '%s,%s-%s'%(session[self.cname],type,id)
        else:
            session[self.cname] = '%s-%s'%(type,id)
        session.save()
        redirect_to(controller='catalog',action='%sdetail'%type.lower(),id=id)

    def removefromcart(self,id):
        type,id = id.split('-')
        c.cart.remove( meta.Session.query(getattr(model,type)).get(id) )
        self.save_cart_cookie()
        redirect_to(controller='catalog',action='%sdetail'%type.lower(),id=id)

    def checkout_with(self,id):
        if self.cname in session:
            session[self.cname] = '%s|Work:%s'%(session[self.cname],id)
        else:
            session[self.cname] = 'Work:%s'%id
        session.save()
        redirect_to(controller='catalog',action='checkout')

    def checkout(self):
        return render('/catalog/checkout.html')
