from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, username, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        username = username
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, username=None, **extra_fileds):
        extra_fileds.setdefault('is_staff', False)
        extra_fileds.setdefault('is_superuser', False)
        return self._create_user(email, password, username, **extra_fileds)

    def create_superuser(self, email, password, username, **extra_fileds):
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_superuser', True)
        if extra_fileds.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        if extra_fileds.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        return self._create_user(email, password, username, **extra_fileds)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("メールアドレス", unique=True)
    username = models.CharField("ユーザー名", max_length=20, unique=True)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "user"




