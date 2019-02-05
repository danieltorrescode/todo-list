from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'users'

urlpatterns = [
    #
    path('',users.as_view(), name='list'),
    #
	# path('edit/<int:pk>/',UsersListEdit.as_view(), name='edit'),
    #
    path('log_in/', log_in.as_view(), name='log_in'),
]
