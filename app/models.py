from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class addClient(models.Model):
    id=models.AutoField(primary_key=True)
    client_name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    objects=models.Manager()

    def __str__(self):
        return self.client_name
    class Meta:
        db_table='addclients'

class addProject(models.Model):
    id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=100)
    contributed_users=models.ManyToManyField(User)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by_client=models.ForeignKey(addClient,unique=False,on_delete=models.CASCADE)
    objects=models.Manager()

    class Meta:
        db_table='addprojects'
    