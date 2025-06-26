from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):

    email = models.EmailField(unique=True, verbose_name="Email", help_text="L'email de l'utilisateur")
    first_name = models.CharField(max_length=30, verbose_name="Prénom", help_text="Prénom")
    last_name = models.CharField(max_length=30, verbose_name="Nom", help_text="Nom de famille")
    is_active = models.BooleanField(default=True, verbose_name="Actif", help_text="Actif")
    is_staff = models.BooleanField(default=False, verbose_name="Admin", help_text="Admin")

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name = 'Cutom User'
        verbose_name_plural = 'Cutom Users'