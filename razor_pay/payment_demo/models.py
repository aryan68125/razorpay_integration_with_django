
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
#CustomUser manager
from payment_demo.user_manager import UserManager
import os
from django.utils.deconstruct import deconstructible
import time
# Create your models here.


class UserMaster(AbstractBaseUser, PermissionsMixin):
    email_id = models.EmailField(unique=True)
    created_by = models.IntegerField(default=1,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateField(null=True,blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email_id
