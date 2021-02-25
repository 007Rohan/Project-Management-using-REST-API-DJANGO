from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('registerClient',v.AddClient.as_view()),
    path('addProject',v.AddProject.as_view()),
    path('clientlist',v.ClientList.as_view()),
    path('deleteClient/<int:pk>',v.DeleteClient.as_view()),
    path('clientprojectlist',v.ClientProjectList.as_view()),
    path('projectlist',v.ProjectList.as_view()),
]