from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.cache import cache

from users.cache_manager import USER_CACHE_PATTERN

UserModel = get_user_model()


class CachedModelBackend(ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        cache_key = USER_CACHE_PATTERN.format(username=username)
        user = cache.get(cache_key)
        if not user:
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
                cache.set(cache_key, user)
            except UserModel.DoesNotExist:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a nonexistent user (#20760).
                UserModel().set_password(password)
        if user:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
