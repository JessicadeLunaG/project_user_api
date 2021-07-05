from rest_framework import serializers
from core.models import User, Project
from user.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    """Serialize a project"""
    author = UserSerializer(many = True)

    class Meta:
        
        model = Project
        fields = (
            'id','project_name', 'project_type', 'schedule', 
            'project_description','creation_date', 'author','project_status'
        )
        read_only_fields = ('project_name',)
    
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return Project.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        
        user = super().update(instance, validated_data)
        user.save()

        return user

class ProjectDetailSerializer(ProjectSerializer):
    """Serialize a recipe detail"""
    
    class Meta:
        model = Project
        fields = (
            'project_name', 'project_type', 'schedule', 
            'project_description','creation_date', 'author','project_status'
        )
