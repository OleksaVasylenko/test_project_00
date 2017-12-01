from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class TestTaskUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Overrides `UserManager._create_user` to set `email` as required field.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = TestTaskUserManager()

    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
