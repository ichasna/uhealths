from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserProfileManger(BaseUserManager):
    use_in_migrations = True

    def create_user(self,username,password):
        user = self.model(username=username,password=password)

        user.set_password(password)
        user.save(using=self._db)
        

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
     username = models.CharField(max_length=20,unique=True)
     password = models.CharField(max_length = 150,unique=True)

     gender = models.CharField('Gender',max_length=6)
     height = models.FloatField('Height',default=0)
     weight = models.FloatField('Weight',default=0)
     age = models.IntegerField('Age',default=0)
     bmi = models.IntegerField('BMI',default=0)
     bmr = models.IntegerField('BMR',default=0)
     
     
     USERNAME_FIELD = 'username'
     PASSWORD_FIELD = 'password'


     objects = UserProfileManger()


     





