from django_productline.context import PRODUCT_CONTEXT

def _override(new, orig):
    '''
    to override original, use a new value that is not None.
    to use the original value, set the new value to None.
    => it is possible to override the original value with an empty string!
    '''
    if new is not None:
        return new
    else:
        return orig


def refine_EMAIL_BACKEND(original):
    return _override(PRODUCT_CONTEXT.EMAIL_BACKEND, original)


def refine_EMAIL_HOST(original):
    return _override(PRODUCT_CONTEXT.EMAIL_HOST, original)


def refine_EMAIL_HOST_USER(original):
    return _override(PRODUCT_CONTEXT.EMAIL_HOST_USER, original)


def refine_EMAIL_HOST_PASSWORD(original):
    return _override(PRODUCT_CONTEXT.EMAIL_HOST_PASSWORD, original)


def refine_EMAIL_PORT(original):
    return _override(PRODUCT_CONTEXT.EMAIL_PORT, original)


def refine_EMAIL_USE_TLS(original):
    return _override(PRODUCT_CONTEXT.EMAIL_USE_TLS, original)

def refine_EMAIL_USE_SSL(original):
    return _override(PRODUCT_CONTEXT.EMAIL_USE_SSL, original)


def refine_DEFAULT_FROM_EMAIL(original):
    return _override(PRODUCT_CONTEXT.DEFAULT_FROM_EMAIL, original)


def refine_SERVER_EMAIL(original):
    return _override(PRODUCT_CONTEXT.SERVER_EMAIL, original)


def refine_EMAIL_SUBJECT_PREFIX(original):
    return _override(PRODUCT_CONTEXT.EMAIL_SUBJECT_PREFIX, original)

