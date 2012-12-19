import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render
from gwhiz import model
import formencode
from formencode import htmlfill
from pylons.decorators import validate
from pylons.decorators.rest import restrict
from gwhiz.model import meta
import gwhiz.lib.helpers as h


log = logging.getLogger(__name__)

class NewPageForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    title = formencode.validators.String(not_empty=True)
    description = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':'Please enter some content for the page.'
        }
    )



class PublicationController(BaseController):

    def view(self, id):
        c.heading = 'heya..'
        pub_q = model.meta.Session.query(model.Publication)
        c.pub = pub_q.get(int(id))
        if c.pub is None:
            abort(404)
        return render('/publication/view.html')

    def new(self):
        return render('/publication/new.html')

    @restrict('POST')
    @validate(schema=NewPageForm(), form='new')
    def create(self):
        # Add the new page to the database
        pub = model.Publication()
        for k, v in self.form_result.items():
            setattr(pub, k, v)
        model.meta.Session.add(pub)
        model.meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='publication',
            action='view', id=pub.id)
        return "Moved temporarily"

    def edit(self, id=None):
        if id is None:
            abort(404)
        pub_q = meta.Session.query(model.Publication)
        pub = pub_q.filter_by(id=id).first()
        if pub is None:
            abort(404)
        values = {
            'title': pub.title,
            'description': pub.description
        }
        return htmlfill.render(render('/publication/edit.html'), values)

    @restrict('POST')
    @validate(schema=NewPageForm(), form='edit')
    def save(self, id=None):
        pub_q = meta.Session.query(model.Publication)
        pub = pub_q.filter_by(id=id).first()
        if pub is None:
            abort(404)
        for k,v in self.form_result.items():
            if getattr(pub, k) != v:
                setattr(pub, k, v)
        meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='publication', action='view',
            id=pub.id)
        return "Moved temporarily"

    def list(self):
        c.pubs = meta.Session.query(model.Publication).all()
        return render('/publication/list.html')
