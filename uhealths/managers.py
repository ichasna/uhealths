import re
from django.contrib.auth.base_user import BaseUserManager  
from django.utils.translation import ugettext_lazy as _  

class UserProfileManger(BaseUserManager):
    def create_user(self,username,password,weight,height,gender):
        user = self.model(username=username,password=password,weight = weight,height=height,gender=gender)
        user.set_password(password)
        user.save()
        return user
