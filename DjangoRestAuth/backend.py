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

from __future__ import unicode_literals

import logging

from django.contrib.auth import get_user_model

from RestAuthCommon.error import InternalServerError

from RestAuthClient.restauth_user import User as RestAuthUser

from DjangoRestAuth.connection import connection

User = get_user_model()
USERNAME_FIELD = username_field = getattr(User, 'USERNAME_FIELD', 'username')
log = logging.getLogger(__name__)


class RestAuthBackend(object):
    def authenticate(self, username=None, password=None):
        if username is None or password is None:
            return None

        ra_user = RestAuthUser(connection, username)

        try:
            verified = ra_user.verify_password(password)
        except InternalServerError as e:
            response = e.args[0]
            log.error('RestAuth returned HTTP 500: %s', response.read())
            return None

        if verified:
            try:
                user = User.objects.get(**{USERNAME_FIELD: username})
            except User.DoesNotExist:
                user = User.objects.create_user(username, password=password)

            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
