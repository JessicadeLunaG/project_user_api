from rest_framework import viewsets,  mixins
from django.shortcuts import render
from rest_framework.response import Response
from core.models import Project
from project import serializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_protect

class CreateProjectViewSet(viewsets.ViewSet):

    serializer_class = serializers.ProjectSerializer
    queryset = Project.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def create(self, serializer):
        """Create a new recipe"""
        #serializer.create(auth=self.request.project)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
@csrf_protect
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        id = request.query_params.get('id', None)
        
        if id is not None:
            projects= projects.filter(title__icontains=id)
        
        project_serializer = serializers.ProjectSerializer(projects, many=True)
        return JsonResponse(project_serializer.data, safe=False)


    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        projects_serializer = serializers.ProjectSerializer(data=project_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse(projects_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(projects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Project.objects.all().delete()
        return JsonResponse({'message': '{} Projects were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try: 
        project = Project.objects.get(pk=pk) 
    except Project.DoesNotExist: 
        return JsonResponse({'message': 'The Project does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        project_serializer = serializers.ProjectSerializer(project) 
        return JsonResponse(project_serializer.data) 
 
    elif request.method == 'PUT': 
        Project_data = JSONParser().parse(request) 
        Project_serializer = serializers.ProjectSerializer(Project, data=Project_data) 
        if Project_serializer.is_valid(): 
            Project_serializer.save() 
            return JsonResponse(Project_serializer.data) 
        return JsonResponse(Project_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        Project.delete() 
        return JsonResponse({'message': 'Project was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def Project_list_published(request):
    Projects = Project.objects.filter(project_status=True)
        
    if request.method == 'GET': 
        Projects_serializer = serializers.ProjectSerializer(Projects, many=True)
        return JsonResponse(Projects_serializer.data, safe=False)