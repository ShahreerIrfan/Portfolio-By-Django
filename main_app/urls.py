
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='edit_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('resume/', views.resume, name='resume'),
    path('add-project/', views.add_project, name='add_project'),
    path('project-list/', views.project_list, name='project_list'),
    path('project-detail/<int:project_id>/', views.project_detail, name='project_detail'),
]