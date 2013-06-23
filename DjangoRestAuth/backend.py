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
        print('authenticate(%s, %s)' % (username, password))
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
