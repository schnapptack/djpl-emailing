from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings

class TextEmail(EmailMessage):
    #content_subtype = 'text/plain'
    pass
    

class HtmlEmail(EmailMessage):
    
    content_subtype = 'html'
    
    def __init__(self, *args, **kwargs):
        template = kwargs.pop('template')
        context = kwargs.pop('context')

        context['brand_bg'] = settings.EMAIL_BRAND_BG
        context['brand_color'] = settings.EMAIL_BRAND_COLOR
        context['link_color'] = settings.EMAIL_LINK_COLOR
        context['footer_content'] = settings.EMAIL_FOOTER_CONTENT

        kwargs['body'] = get_template(template).render(Context(context))
        super(HtmlEmail, self).__init__(*args, **kwargs)
    


        
        
        

        
        
       


