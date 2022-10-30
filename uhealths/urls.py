from django.urls import path
from . import views

app_name = 'uhealths'

urlpatterns = [
    path('', views.landingpage, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('check/',views.check_healths_status,name='check'),
    path('update/',views.update_data,name='update_data')
]