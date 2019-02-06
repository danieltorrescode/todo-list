from django.contrib import admin
from django.urls import path
from .views import *
app_name = 'tasks'

urlpatterns = [
    #
    path('',tasks.as_view(), name='list'),
    #
	path('edit/<int:pk>/',TasksListEdit.as_view(), name='edit'),
]
