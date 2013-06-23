Settings
--------

.. _settings-restauth_connections:

RESTAUTH_CONNECTIONS
____________________

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
