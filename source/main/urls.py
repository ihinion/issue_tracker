"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView, ProjectListView, \
    ProjectView, ProjectCreateView, ProjectTaskCreateView, ProjectUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('add/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('projects/', ProjectListView.as_view(), name='projects_list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/tasks/add/', ProjectTaskCreateView.as_view(),
         name='project_task_add'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update')
]
