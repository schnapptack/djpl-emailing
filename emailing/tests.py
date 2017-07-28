from django.test import TestCase, override_settings
from django_productline.testingutils import NoMigrationsTestCase
from emailing.emails import HtmlEmail


class SignupMailTest(NoMigrationsTestCase):
    """
    This is a helper test class which allows us to programmatically send emails for proper viewing
    """

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend')
    def test_send_email(self):
        msg = HtmlEmail(
            subject='test',
            template='emailing/testmail.html',
            context=dict(),
            to=['toni@schnapptack.de', ]
        )
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)
