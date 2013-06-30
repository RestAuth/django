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


.. _settings-restauth_local_password:

RESTAUTH_LOCAL_PASSWORDS
________________________

Default::

   False

If set to ``True``, passwords will be stored in your local database.

By default, pssword are not stored in your local database, meaning that no
password hashes can be stolen from you if your site is compromised (Unless, of
course, your RestAuth server is also compromised). The downside is that users
will be unable to log in if your RestAuth server is unavailable for some reason.

If you set this value to ``True``, DjangoRestAuth will set the password via
:py:meth:`set_password
<Django:django.contrib.auth.models.AbstractBaseUser.set_password>` whenever a
user logs in.

RESTAUTH_USER_GROUP_FIELDS
__________________________

Default::
   {
       'staff': 'is_staff',
       'admin': 'is_admin',
   }

