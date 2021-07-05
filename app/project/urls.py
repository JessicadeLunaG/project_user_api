from django.urls import path, include
from rest_framework import routers
from project import views

from django.conf.urls import url 


router = routers.DefaultRouter()
router.register('new', views.CreateProjectViewSet)

app_name = 'project'

""" urlpatterns = [
    path('', include(router.urls)),
    url(r'^what/$', views.project_list),
] 
 """
urlpatterns = [
    
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.project_detail),
    #url('api/tutorials/published', views.Project_list_published),
    url('projectlist/', views.project_list),
    url('aver/', include(router.urls)),
]

