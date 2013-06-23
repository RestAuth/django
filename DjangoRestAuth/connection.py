# -*- coding: utf-8 -*-
#
# This file is part of DjangoRestAuth (https://django.restauth.net).
#
# DjangoRestAuth is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DjangoRestAuth is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DJANGORestAuth.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from RestAuthClient.common import RestAuthConnection

DEFAULT_RESTAUTH_ALIAS = 'default'


def get_connection(alias):
    try:
        conf = settings.RESTAUTH_CONNECTIONS[alias]

        return RestAuthConnection(
            host=conf['HOST'],
            user=conf['USER'],
            passwd=conf['PASSWORD'],
            content_handler=conf.get('CONTENT_HANDLER'),  # optional
        )
    except KeyError:
        raise ImproperlyConfigured("Unknown RestAuth connection requested.")

if DEFAULT_RESTAUTH_ALIAS not in settings.RESTAUTH_CONNECTIONS:
    raise ImproperlyConfigured("No 'default' RestAuth connection configured.")

connection = get_connection(DEFAULT_RESTAUTH_ALIAS)
