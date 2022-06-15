from django.contrib.auth.models import User
from rest_framework import serializers
from projects.models import Project, Rating, Label
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='users-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

   