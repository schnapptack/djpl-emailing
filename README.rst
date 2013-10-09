djpl-emailing
===========================

a couple of features for django-productline to configure email.

License: MIT


Feature ``emailing``
-----------------------

 provides a basic email configuration(django default) for other features to refine.

Can be used as a base for ``emailing.features.contextconf``, ``emailing.features.console``, and/or
other features to adapt the email configuration to the specific setup.

Feature ``emailing.features.contextconf``
------------------------------------------

 allows email configuration via product context

This feature refines the email settings to use values given in the product context.

*requires features:* 

- ``emailing``

*requires product context keys:*

- ``EMAIL_BACKEND``
- ``EMAIL_HOST``
- ``EMAIL_HOST_USER``
- ``EMAIL_HOST_PASSWORD``
- ``EMAIL_PORT``
- ``EMAIL_USE_TLS``
- ``DEFAULT_FROM_EMAIL``
- ``SERVER_EMAIL``
- ``EMAIL_SUBJECT_PREFIX``

See https://docs.djangoproject.com/en/dev/ref/settings/

.. note::

    If a value is specified as ``null`` in the product context, the value defined by the original implementation is used.


Feature ``emailing.features.console``
----------------------------------------

use ``django.core.mail.backends.console.EmailBackend`` as ``EMAIL_BACKEND`` to print emails on stdout instead of sending them.
Useful during development/debugging to switch between backends by toggling the feature.
