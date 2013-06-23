from django.contrib.auth import get_user_model

from RestAuthClient.restauth_user import User as RestAuthUser

from DjangoRestAuth.connection import connection

User = get_user_model()
USERNAME_FIELD = username_field = getattr(User, 'USERNAME_FIELD', 'username')


class RestAuthBackend(object):
    def authenticate(self, username=None, password=None):
        if username is None or password is None:
            return None

        ra_user = RestAuthUser(connection, username)
        if ra_user.verify_password(password):
            try:
                user = User.objects.get(**{USERNAME_FIELD: username})
            except User.DoesNotExist:
                user = User.objects.create()

            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
