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

Configure your RestAuth connection. This setting is mandatory!

Available keys:

**HOST**
   The host of the RestAuth server.
**USER**
   The username to use in service authentication.
**PASSWORD**
   The password to use in service authentication.
**CONTENT_HANDLER**
   Optional, if your RestAuth server does not support the default JSON content
   handler. Might be a mime-type defined in :py:data:`CONTENT_HANDLERS
   <RestAuthCommon:RestAuthCommon.handlers.CONTENT_HANDLERS>` or an instance of
   an implementatation of :py:class:`ContentHandler
   <RestAuthCommon:RestAuthCommon.handlers.ContentHandler>`.


.. _settings-restauth_password_field:

RESTAUTH_PASSWORD_FIELD
_______________________

Default::

   ''

By default, Django will not store password hashes in its local database. This
has the advantage that no password hashes can be stolen from you if your site is
compromised (Unless, of course, your RestAuth server is also compromised). The
downside is that users will be unable to log in if your RestAuth server is
unavailable for some reason.

If you set this value to a non-empty string, DjangoRestAuth will pass the
password to :py:meth:`create_user
<Django:django.contrib.auth.models.CustomUserManager.create_user>`, the name of
the keyword argument will be the value of ``RESTAUTH_PASSWORD_FIELD``.

The correct value of this setting depends on your user model. If you haven't
customized your model or inherit from :py:class:`AbstractBaseUser
<Django:django.contrib.auth.models.AbstractBaseUser>`, the correct value is
``password``. Please read the documentation on `customizing authentication
<https://docs.djangoproject.com/en/dev/topics/auth/customizing/>`_ for further
information.
