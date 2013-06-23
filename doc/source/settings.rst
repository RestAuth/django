Settings
--------

.. _settings-restauth_connections:

RESTAUTH_CONNECTIONS
____________________

Default::

   None

Example:

.. code-block:: python

   RESTAUTH_CONNECTIONS = {
       'default': {
           'HOST': 'https://auth.example.com',
           'USER': 'example.com',
           'PASSWORD': '...',
           # OPTIONAL: Use a different content-handler:
           #'CONTENT_HANDLER': 'application/yaml',
       }
   }

.. _settings-restauth_password_field:

RESTAUTH_PASSWORD_FIELD
_______________________

Default::

   ''

If set to a non-empty string, DjangoRestAuth will pass passwords to the
``create_user`` method. The name of the keyword argument will be the value
of this setting.
