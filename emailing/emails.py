# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
import premailer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, os
import logging
# we dont want these warnings on our console output (e.g. in test cases)
import cssutils
cssutils.log.setLevel(logging.CRITICAL)

class TextEmail(EmailMessage):
    #content_subtype = 'text/plain'
    pass


class HtmlEmail(EmailMessage):

    content_subtype = 'html'

    def __init__(self, *args, **kwargs):
        template = kwargs.pop('template', 'emailing/base.html')
        context = kwargs.pop('context', dict())


        context['brand_bg'] = settings.EMAIL_BRAND_BG
        context['button_bg'] = settings.EMAIL_BUTTON_BG
        context['body_bg'] = settings.EMAIL_BODY_BG
        context['brand_color'] = settings.EMAIL_BRAND_COLOR
        context['link_color'] = settings.EMAIL_LINK_COLOR
        context['footer_content'] = settings.EMAIL_FOOTER_CONTENT
        context['logo_src'] = settings.EMAIL_LOGO_SRC
        context['logo_href'] = settings.EMAIL_LOGO_HREF
        context['logo_alignment'] = settings.EMAIL_LOGO_ALIGNMENT
        context['logo_alt_text'] = settings.EMAIL_LOGO_ALT_TEXT

        kwargs['body'] = premailer.transform(get_template(template).render(context))

        super(HtmlEmail, self).__init__(*args, **kwargs)


    def send(self, *args, **kwargs):
        kwargs['fail_silently'] = False
        if not settings.DEBUG:
            try:
                super(HtmlEmail, self).send(*args, **kwargs)
            except Exception:
                # this is a fallback trying to ensure that emails are sent out in case something goes
                # wrong with default implementation.
                if settings.FALLBACK_EMAIL != 'webmaster@localhost':
                    fallback_mail = settings.FALLBACK_EMAIL
                else:
                    fallback_mail = settings.SERVER_EMAIL
                smtpObj = smtplib.SMTP('localhost')
                msg = MIMEMultipart('alternative')
                msg.attach(MIMEText(self.body.encode('utf-8'), 'html', 'utf-8'))
                msg['From'] = fallback_mail
                msg['To'] = fallback_mail
                msg['Subject'] = u"Error sending Email from " + str(self.from_email) + " to " + str(self.to) + " in container " + os.environ['CONTAINER_DIR']
                smtpObj.sendmail(fallback_mail, fallback_mail, msg.as_string())
        else:
            super(HtmlEmail, self).send(*args, **kwargs)
