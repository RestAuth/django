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

from django.contrib.auth.models import Group
from django.core.cache import cache
from django.utils import six

from RestAuthCommon.error import InternalServerError

from RestAuthClient.restauth_user import User as RestAuthUser

from DjangoRestAuth import conf
from DjangoRestAuth.conf import User
from DjangoRestAuth.connection import connection

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
            kwargs = {
                conf.USERNAME_FIELD: username,
            }

            try:
                user = User.objects.get(**kwargs)
            except User.DoesNotExist:
                user = User(**kwargs)

            if conf.LOCAL_PASSWORDS:
                user.set_password(password)

            if conf.SYNC_GROUPS:
                username = getattr(user, conf.USERNAME_FIELD)
                cache_key = '%s-restauth-groups' % username

                groups = cache.get(cache_key)
                if groups is None:
                    groups = [g.name for g in ra_user.get_groups()]
                    cache.set(cache_key, groups)

                self._sync_group_fields(user, groups)
                self._sync_groups(user, groups)


            user.save()

            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def _sync_group_fields(self, user, groups):
        """Synchronize group fields defined by RESTAUTH_USER_GROUP_FIELDS."""

        if not conf.USER_GROUP_FIELDS:
            return

        for groupname, user_field in six.iteritems(conf.USER_GROUP_FIELDS):
            if groupname in groups:
                setattr(user, user_field, True)
            else:
                setattr(user, user_field, False)

    def _sync_groups(self, user, groups):
        groups = [Group.objects.get_or_create(name=name)[0]
                  for name in groups if name not in conf.USER_GROUP_FIELDS]
        user.groups.clear()
        if groups:
            user.groups.add(*groups)
