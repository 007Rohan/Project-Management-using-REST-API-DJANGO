from rest_framework import serializers
from .models import addClient,addProject
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']


class ClientSerializer(serializers.ModelSerializer): 
    class Meta:
        model=addClient
        fields=['id','client_name','created_at','created_by']

class ClientProjectSerializer(serializers.ModelSerializer):
    contributed_users = UserSerializer(many=True)
    class Meta:
        model=addProject
        fields='__all__'
class ClientProjectSerializer1(serializers.ModelSerializer):
    class Meta:
        model=addProject
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=addProject
        fields=['id','project_name','created_at','created_by_client']
