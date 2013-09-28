from django_productline.context import PRODUCT_CONTEXT


# Alternate email backend:
#   'django.core.mail.backends.console.EmailBackend'
#   'django.core.mail.backends.filebased.EmailBackend'
#   'django.core.mail.backends.locmem.EmailBackend'
#   'django.core.mail.backends.locmem.EmailBackend'

introduce_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
introduce_EMAIL_HOST = None
introduce_EMAIL_HOST_USER = None
introduce_EMAIL_HOST_PASSWORD = None
introduce_EMAIL_PORT = None
introduce_EMAIL_USE_TLS = True
introduce_DEFAULT_FROM_EMAIL = None
introduce_SERVER_EMAIL = None
introduce_EMAIL_SUBJECT_PREFIX = None

