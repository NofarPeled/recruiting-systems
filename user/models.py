from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from common.language import Languages
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(_('First Name'), max_length=50, blank=False, null=False)
    last_name = models.CharField(_('Last Name'), max_length=50, blank=False, null=False)
    username = models.CharField(_('User Name'), max_length=50, unique=True)
    email= models.CharField(_('Email'), unique=True, blank=False, max_length=254,null=False)
    password = models.CharField(_('Password'), max_length=100, blank=False, null=False)

    language = models.CharField(_('Language'), max_length=2, choices=Languages.choices, default=Languages.EN)

    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['first_name', 'last_name', 'password', 'username', ]

    objects = UserManager()


