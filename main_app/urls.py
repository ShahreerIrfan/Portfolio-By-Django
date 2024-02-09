
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('resume/', views.resume, name='resume'),
    path('add-project/', views.add_project, name='add_project'),
    path('project-list/', views.project_list, name='project_list'),
    path('project-detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]