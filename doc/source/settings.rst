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


.. _settings-restauth_local_passwords:

RESTAUTH_LOCAL_PASSWORDS
________________________

Default::

   False

If set to ``True``, passwords will be stored in your local database.

By default, passwords are not stored in your local database, meaning that no
password hashes can be stolen from you if your site is compromised (Unless, of
course, your RestAuth server is also compromised). The downside is that users
will be unable to log in if your RestAuth server is unavailable for some reason.

If you set this value to ``True``, DjangoRestAuth will set the password via
:py:meth:`set_password
<Django:django.contrib.auth.models.AbstractBaseUser.set_password>` whenever a
user logs in.

.. _settings-restauth_user_group_fields:

RESTAUTH_USER_GROUP_FIELDS
__________________________

Default::

   {
       'staff': 'is_staff',
       'admin': 'is_admin',
   }

.. NOTE::

   This setting is only used if :ref:`settings-RESTAUTH_SYNC_GROUPS` is ``True``.

A dictionary of RestAuth groups that are not stored as standard Django user
groups but as model fields of the user instance. A field is set to ``True`` if a
user is in the named group or ``False`` otherwise.

The default means that a users ``is_staff`` field is set to ``True`` if she/he
is a member of the ``staff`` RestAuth group, likewise for ``admin`` and
``is_admin``.

.. _settings-restauth_sync_groups:

RESTAUTH_SYNC_GROUPS
____________________

Default::

   True

If set to ``False``, groups will not be synchronized with RestAuth.

By default, groups are synchronized with groups found in RestAuth. User fields
are set according to :ref:`settings-restauth_user_group_fields` and all other
RestAuth groups are synchronized with Djangos standard user groups.

