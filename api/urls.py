from sys import prefix
from rest_framework.routers import DefaultRouter
from .views import ProjectViewset, RatingViewset, LabelViewset, UserCreate, LoginAPI, ProfileViewset
from django.urls import path
from rest_framework.authtoken import views
from knox import views as knox_views


router = DefaultRouter()
router.register('projects', ProjectViewset, basename='projects')
router.register('ratings', RatingViewset, basename='ratings')
router.register('labels', LabelViewset, basename='labels')
# router.register('profile', ProfileViewset, basename='profile')

urlpatterns = [
    # path("", APIRootView(), name='api-root'),
    path("users/", UserCreate.as_view(), name="user_create"),
    path('login/', LoginAPI.as_view(), name='login'),
    path('profile/', ProfileViewset.as_view(), name='profile'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


]

urlpatterns += router.urls
