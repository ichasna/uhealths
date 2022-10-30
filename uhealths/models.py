
from email.policy import default
from random import choices
import re
from django.db import models
from django.contrib.auth.models import User


class HealthStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_update = models.DateField(auto_now_add=True)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    
    gender = models.CharField(max_length=6)
    bmr = models.FloatField()
    bmi = models.FloatField()
    calori_intake = models.FloatField(default=0)
    
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_bmi(self):
        return self.bmi
    
