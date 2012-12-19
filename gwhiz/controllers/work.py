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

class WorkController(BaseController):

    def index(self):
        return self.list()

    def view(self, id):
        c.heading = 'work details'
        work_q = model.meta.Session.query(model.Work)
        c.work = work_q.get(int(id))
        if c.work is None:
            abort(404)
        return render('/work/view.html')

    def new(self):
        return render('/work/new.html')

    @restrict('POST')
    @validate(schema=NewPageForm(), form='new')
    def create(self):
        # Add the new page to the database
        work = model.Work()
        for k, v in self.form_result.items():
            setattr(work, k, v)
        model.meta.Session.add(work)
        model.meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='work',
            action='view', id=work.id)
        return "Moved temporarily"

    def edit(self, id=None):
        if id is None:
            abort(404)
        work_q = meta.Session.query(model.Work)
        work = work_q.filter_by(id=id).first()
        if work is None:
            abort(404)
        values = {
            'title': work.title,
            'description': work.description
        }
        return htmlfill.render(render('/work/edit.html'), values)

    @restrict('POST')
    @validate(schema=NewPageForm(), form='edit')
    def save(self, id=None):
        work_q = meta.Session.query(model.Work)
        work = work_q.filter_by(id=id).first()
        if work is None:
            abort(404)
        for k,v in self.form_result.items():
            if getattr(work, k) != v:
                setattr(work, k, v)
        meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='work', action='view',
            id=work.id)
        return "Moved temporarily"

    def list(self):
        c.works = meta.Session.query(model.Work).all()
        return render('/work/list.html')
