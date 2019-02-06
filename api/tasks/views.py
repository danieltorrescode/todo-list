from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.mixins import (
    CreateModelMixin,DestroyModelMixin,UpdateModelMixin
)
from .permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import *

class tasks(CreateModelMixin,ListAPIView):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = Task.objects.filter(user=request.user).order_by('id')
        serializer = TaskSerializer(queryset,many=True)
        return Response(serializer.data)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TasksListEdit(DestroyModelMixin,UpdateModelMixin,RetrieveAPIView):
    queryset = Task
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)