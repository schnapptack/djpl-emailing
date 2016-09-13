from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings
from premailer import transform
import smtplib

class TextEmail(EmailMessage):
    #content_subtype = 'text/plain'
    pass


class HtmlEmail(EmailMessage):

    content_subtype = 'html'

    def __init__(self, *args, **kwargs):
        template = kwargs.pop('template')
        context = kwargs.pop('context')

        context['brand_bg'] = settings.EMAIL_BRAND_BG
        context['body_bg'] = settings.EMAIL_BODY_BG
        context['brand_color'] = settings.EMAIL_BRAND_COLOR
        context['link_color'] = settings.EMAIL_LINK_COLOR
        context['footer_content'] = settings.EMAIL_FOOTER_CONTENT

        kwargs['body'] = transform(get_template(template).render(Context(context)))
        super(HtmlEmail, self).__init__(*args, **kwargs)


    def send(self, *args, **kwargs):
        try:
            super(HtmlEmail, self).send(*args, **kwargs)
        except smtplib.SMTPException:
            smtpObj = smtplib.SMTP('localhost')
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Error sending Email from " + self.from_email + " to " + self.to + " in container " + os.environ['CONTAINER_DIR']
            msg['From'] = settings.DEFAULT_FROM_EMAIL
            msg['To'] = settings.SERVER_EMAIL
            msg.attach(MIMEText(self.body, 'html'))
            smtpObj.sendmail(settings.DEFAULT_FROM_EMAIL, settings.SERVER_EMAIL, msg.as_string())
            raise
