from .models import Task,AuthUser
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model=AuthUser
        fields='__all__'