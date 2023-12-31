# Generated by Django 4.2.4 on 2023-09-11 07:04

from django.db import migrations, models
import django.db.models.deletion
import house.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to=house.models.GenerateProfileImagePath())),
                ('description', models.TextField()),
                ('point', models.IntegerField(default=0)),
                ('completed_tasks_count', models.IntegerField(default=0)),
                ('not_completed_tasks_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manager', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_house', to='users.profile')),
            ],
        ),
    ]
