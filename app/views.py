from django.shortcuts import render,HttpResponse

from rest_framework import generics
from .models import addClient,addProject
from .serializer import ClientSerializer,ProjectSerializer,ClientProjectSerializer,ClientProjectSerializer1
# Create your views here.

def home(request):
    return render(request,"index.html")

class AddClient(generics.CreateAPIView):
    serializer_class=ClientSerializer

class AddProject(generics.CreateAPIView):
    serializer_class=ClientProjectSerializer1

class ClientList(generics.ListAPIView):
    queryset=addClient.objects.all()
    serializer_class=ClientSerializer

class DeleteClient(generics.DestroyAPIView):
    queryset=addClient.objects.all()
    serializer_class=ClientSerializer

class ProjectList(generics.ListAPIView):
    queryset=addProject.objects.all()
    serializer_class=ProjectSerializer

class ClientProjectList(generics.ListAPIView):
    queryset=addProject.objects.all()
    serializer_class=ClientProjectSerializer


