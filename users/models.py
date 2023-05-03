from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.models import User, PermissionsMixin, make_password
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.cache_manager import invalidate_user_cache


class MaralUserManager(BaseUserManager):

    def create_user(self, email=None, password=None, is_active=True, is_staff=True, is_admin=False):
        if not email:
            raise ValueError("Please Provide An Email Address.")
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, password, email=None):
        user = self.create_user(
            email=email,
            password=password,
            is_admin=True,
            is_active=True,
            is_staff=True
        )
        return user


class MaralUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = MaralUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
        invalidate_user_cache(self.email)
