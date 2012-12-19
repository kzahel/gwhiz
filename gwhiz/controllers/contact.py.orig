import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from gwhiz.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ContactController(BaseController):

    def index(self):
        return render('/contact/form.html')

    def send(self):
        name = request.params.get('name')
        email = request.params.get('email')
        message = request.params.get('message')
        subscribe = request.params.get('subscribe')
        try:
            import smtplib
            server = smtplib.SMTP('localhost')
            server.sendmail('webform@gwhiz.com','kgraehl@gmail.com','reply-to:%s\nSubject:Message from gwhiz.com web form\nFrom %s (%s)\n%s\nsubscribe:%s'%(email,name,email,message,subscribe))
        except:
            pass

        redirect_to('/contact/thanks')

    def thanks(self):
        return render('/contact/thanks.html')

    def old_dontuse_submit(self):
        c.form_msg = ''
        name = request.params.get('name')
        email = request.params.get('email')
        message = request.params.get('message')
        if not email:
            c.form_msg = "Please enter a value"
        elif '@' not in email:
            c.form_msg = "An email address must contain at least one '@' character."
        else:
            domain = email.split('@')[1]
            if '.' not in domain:
                c.form_msg = "An email address domain must contain "
                c.form_msg += "at least one '.' character."
            if not domain.split('.')[-1]:
                c.form_msg = "Please specify a domain type after the '.' character"
        if c.form_msg:
            c.email_value = email
            #return render('/contact/base.html')
            redirect_to('/contact')
        redirect_to('/contact/thanks')
        #return 'Your email is: %s' % request.params['email']


