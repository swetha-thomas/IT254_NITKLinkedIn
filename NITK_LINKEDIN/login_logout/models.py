from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

# class CustomAccountManager(BaseUserManager):
#   def create_user(self, email, password, **other_fields):
    
#     if not email:
#       raise ValueError('You must provide a valid email')
    
#     email = self.normalize_email(email)
#     user = self.model(email=email, **other_fields)
#     user.set_password(password)
#     user.save()
#     return user
  
#   def create_superuser(self, email, password, **other_fields):
#     other_fields.setdefault('is_staff', True)
#     other_fields.setdefault('is_superuser', True)
#     other_fields.setdefault('is_active', True)
    
#     return self.create_user(email, password, **other_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#   is_student = models.BooleanField(default=False)
#   is_organization = models.BooleanField(default=False)
#   email = models.EmailField('email address', unique=True)
#   start_date = models.DateTimeField(default=timezone.now)
#   is_staff = models.BooleanField(default=False)
#   is_active = models.BooleanField(default=False)
  
#   objects = CustomAccountManager()
  
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = []
