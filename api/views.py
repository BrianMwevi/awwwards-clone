from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from projects.models import Project, Rating, Label
from .serializers import UserSerializer, ProjectSerializer, RatingSerializer, LabelSerializer
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.models import User

from accounts.models import Profile
from .serializers import ProfileSerializer

from rest_framework import permissions, serializers, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken

from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response


# Create your views here.
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
