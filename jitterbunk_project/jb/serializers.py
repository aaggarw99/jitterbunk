from django.contrib.auth.models import User
from .models import Bunk, UserProfile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'photo']

class BunkSerializer(serializers.ModelSerializer):
    from_user = UserProfileSerializer()
    to_user = UserProfileSerializer()

    class Meta:
        model = Bunk
        fields = ['id', 'from_user', 'to_user', 'timestamp']