# Generated by Django 3.1.6 on 2021-02-25 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='addClient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'addclients',
            },
        ),
        migrations.CreateModel(
            name='addProject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contributed_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('created_by_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.addclient')),
            ],
            options={
                'db_table': 'addprojects',
            },
        ),
    ]
