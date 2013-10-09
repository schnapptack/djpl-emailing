#explicitely introduce global email settings here, that other features
#are able to use refinements consistently (from a django perspective this seems redundant)

introduce_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
introduce_EMAIL_HOST = 'localhost'
introduce_EMAIL_HOST_USER = ''
introduce_EMAIL_HOST_PASSWORD = ''
introduce_EMAIL_PORT = 25
introduce_EMAIL_USE_TLS = False
introduce_DEFAULT_FROM_EMAIL = 'webmaster@localhost'
introduce_SERVER_EMAIL = 'root@localhost'
introduce_EMAIL_SUBJECT_PREFIX = '[Django] '

