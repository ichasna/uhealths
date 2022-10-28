from django.urls import path
from . import views

app_name = 'uhealths'

urlpatterns = [
    path('', views.landingpage, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
<<<<<<< HEAD
    path('logout/', views.logout_user, name='logout')
    
=======
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.main_menu, name='menu')
>>>>>>> 54429b6c447b08fc62df2e1ae1eb545de7190ea1
]