from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage


class TextEmail(EmailMessage):
    #content_subtype = 'text/plain'
    pass
    

class HtmlEmail(EmailMessage):
    
    content_subtype = 'html'
    
    def __init__(self, *args, **kwargs):
        template = kwargs.pop('template')
        context = kwargs.pop('context')
        kwargs['body'] = get_template(template).render(Context(context))
        super(HtmlEmail, self).__init__(*args, **kwargs)
    


        
        
        

        
        
       


