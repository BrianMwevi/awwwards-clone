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


class ProfileViewset(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        user = Profile.objects.get(user=request.user)
        data = ProfileSerializer(user, context={'request': request}).data

        return Response(data, status=status.HTTP_200_OK)
    # TODO: Add permission to only request own's profile


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # "token": AuthToken.objects.create(user)[1]
        })


class LabelViewset(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LabelSerializer

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project'])
        serializer.save(project=project)


class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

