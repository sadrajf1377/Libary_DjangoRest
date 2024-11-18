from django.contrib.auth.models import AbstractUser
from rest_framework import serializers


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=AbstractUser
        fields=['username']
