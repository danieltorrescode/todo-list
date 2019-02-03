from django.contrib import admin
from django.urls import path
from . import views
from .views import *
app_name = 'users'

urlpatterns = [
    #
    path('sign_up/', sign_up.as_view(), name='sign_up'),
    #
    path('log_in/', log_in, name='log_in'),
    #
    path('log_out/', log_out, name='log_out'),
]
