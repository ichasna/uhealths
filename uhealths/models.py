from enum import unique
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
class UserProfileManger(BaseUserManager):
    use_in_migrations = True

    def create_user(self,username,password,weight,height,gender):
        user = self.model(username=username,password=password,weight = weight,height=height,gender=gender)

        user.set_password(password)
        user.save(using=self._db)
        

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
     username = models.CharField(max_length=20,unique=True)
     password = models.CharField(max_length = 20,unique=True)

     gender = models.CharField('Gender',max_length=6)
     height = models.FloatField('Height')
     weight = models.FloatField('Weight')
     age = models.IntegerField('Age')
     bmi = models.IntegerField('BMI')
     bmr = models.IntegerField('BMR')
     
     USERNAME_FIELD = 'username'
     PASSWORD_FIELD = 'password'


     objects = UserProfileManger()


     





