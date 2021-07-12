from rest_framework import serializers
from core.models import User, Project
from user.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    """Serialize a project"""

    class Meta:
        
        model = Project
        fields = (
            'id','project_name', 'project_type', 'schedule', 
            'project_description','creation_date','project_status','users'
        )
        read_only_fields = ('project_name',)

class ProjectDetailSerializer(serializers.ModelSerializer):
    """Serialize a recipe detail"""
    #author = UserSerializer(many = True)
    class Meta:
        model = Project
        fields = (
            'id','project_name', 'project_type', 'schedule', 
            'project_description','creation_date','project_status'
        )
        read_only_fields = ('id',)