from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given username, email, and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='Почта', unique=True)
    phone = models.CharField(verbose_name='', max_length=20, null=True, blank=True)
    date_of_birth = models.DateTimeField(verbose_name="дата рождения", null=True, blank=True)
    date_of_change = models.DateTimeField(verbose_name="дата изменения", null=True, blank=True)
    date_of_creation = models.DateTimeField(verbose_name="дата создания", auto_created=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

