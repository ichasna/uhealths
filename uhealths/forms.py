from tkinter import Widget
from uhealths.models import HealthStats
from django import forms
class HealthStatsForm(forms.ModelForm):
    class Meta:
        model = HealthStats
        exclude = ('bmi','bmr')
        #fields = ['text']
        CHOICES=[('Male','Male'),
         ('Female','Female')]
        widgets ={
            'gender': forms.RadioSelect(choices= CHOICES,
            attrs={
            'id': 'gender', 
            'name': 'gender',

            }),
            'weight': forms.IntegerField(attrs={
                'id':'weight',
                'name': 'weight',
                
            }),
            'height': forms.IntegerField(attrs={
                'id': 'height',
                'name': 'height',
            }),
            'age': forms.IntegerField(attrs={
                'id': 'age',
                'name': 'age',

            })
        }
        
        gender = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))
      