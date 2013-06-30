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

from django.conf import settings
from django.contrib.auth import get_user_model


# base user model settings
User = get_user_model()
USERNAME_FIELD = username_field = getattr(User, 'USERNAME_FIELD', 'username')

# Some RestAuth settings
LOCAL_PASSWORDS = getattr(settings, 'RESTAUTH_LOCAL_PASSWORDS', False)

# map some groups to user fields:
USER_GROUP_FIELDS = getattr(settings, 'RESTAUTH_USER_GROUP_FIELDS', {
    'staff': 'is_staff',
    'admin': 'is_admin',
})
