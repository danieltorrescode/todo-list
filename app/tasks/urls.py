from django.contrib import admin
from django.urls import path
from . import views
from .views import *
app_name = 'tasks'

urlpatterns = [
    #
    path('', views.index, name='index'),
    #
    path('tasks/',tasks.as_view(), name='list'),
    #
    path('tasks/create/',create.as_view(), name='create'),
    #
    path('tasks/delete/<int:pk>/',delete.as_view(), name='delete'),
	#
	path('tasks/update/<int:pk>/',update.as_view(), name='update'),
]
