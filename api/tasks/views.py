from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.mixins import (
    CreateModelMixin,DestroyModelMixin,UpdateModelMixin
)
from .serializers import *
from .models import *

class tasks(CreateModelMixin,ListAPIView):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TasksListEdit(DestroyModelMixin,UpdateModelMixin,RetrieveAPIView):
    queryset = Task
    serializer_class = TaskSerializer

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)