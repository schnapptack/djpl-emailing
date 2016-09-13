# coding=utf-8
from __future__ import unicode_literals

def refine_INSTALLED_APPS(original):
    return ['emailing'] + list(original)



# explicitely introduce global email settings here, that other features
# are able to use refinements consistently (from a django perspective this seems redundant)

introduce_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
introduce_EMAIL_HOST = 'localhost'
introduce_EMAIL_HOST_USER = ''
introduce_EMAIL_HOST_PASSWORD = ''
introduce_EMAIL_PORT = 25
introduce_EMAIL_USE_TLS = False
introduce_DEFAULT_FROM_EMAIL = 'webmaster@localhost'
introduce_SERVER_EMAIL = 'root@localhost'
introduce_EMAIL_SUBJECT_PREFIX = '[Django] '

# these colors are used to brand the email appearance
introduce_EMAIL_BRAND_BG = '#444'
introduce_EMAIL_BRAND_COLOR = '#fff'
introduce_EMAIL_BODY_BG = '#f6f6f6'
introduce_EMAIL_LINK_COLOR = '#417690'
introduce_EMAIL_FOOTER_CONTENT = '''
    <p>schnapptack GmbH | Schulze-Delitzsch-Straße 13 | 70565 Stuttgart</p>
    <p><a href="http://schnapptack.de">www.schnapptack.de</a></p>
'''
