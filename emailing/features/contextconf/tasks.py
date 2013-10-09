
def refine_get_context_template(original):
    '''
    Refines ``ape.helpers.get_context_template`` and adds email configuration context keys.
    '''

    def get_context_template():
        return dict(original(), **dict(
            EMAIL_BACKEND=None,
            EMAIL_HOST=None,
            EMAIL_HOST_USER=None,
            EMAIL_HOST_PASSWORD=None,
            EMAIL_PORT=None,
            EMAIL_USE_TLS=None,
            DEFAULT_FROM_EMAIL=None,
            SERVER_EMAIL=None,
            EMAIL_SUBJECT_PREFIX=None,
        ))

    return get_context_template
