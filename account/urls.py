from .views import *
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login,name='login'),
]
