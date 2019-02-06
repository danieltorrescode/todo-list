from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *

class TaskSerializer(ModelSerializer):
    # status = SerializerMethodField()
    class Meta:
        model = Task
        fields = [
            'id',
            'name',
            'status',
        ]

    # def get_status(self,obj):
    #     return obj.get_status_display()