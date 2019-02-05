from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.mixins import (
    CreateModelMixin,DestroyModelMixin,UpdateModelMixin
)
from .serializers import *
from django.contrib.auth.models import User

class users(CreateModelMixin,ListAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class log_in(APIView):
    permission_classes = [AllowAny]
    queryset = User
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# class UsersListEdit(DestroyModelMixin,UpdateModelMixin,RetrieveAPIView):
#     queryset = User
#     serializer_class = UserSerializer

#     def put(self, request, *args, **kwargs):
#         self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         self.destroy(request, *args, **kwargs)
