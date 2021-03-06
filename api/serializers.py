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

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        # Token.objects.create(user=user)
        return user


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='ratings-detail')
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all())
    user = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = [
            'project',
            'rating',
            'id',
            'user',
            'design',
            'usability',
            'creativity',
            'content',
            'posted_at',
            'url',
        ]

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'image': obj.user.profile.image.url
        }


class LabelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Label
        fields = [
            'id',
            'name',
            'created_at'
        ]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='projects-detail')
    user = user = serializers.SerializerMethodField()
    ratings = RatingSerializer(many=True, read_only=True, required=False)
    labels = LabelSerializer(many=True, read_only=True, required=False)
    posted_at = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'average_rating',
            'ratings',
            'design',
            'creativity',
            'usability',
            'content',
            'user',
            'labels',
            'image',
            'posted_at',
            'url',
        ]

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'image': obj.user.profile.image.url
        }

    def get_posted_at(self, obj):
        return obj.posted_at.strftime('%Y-%m-%d')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'projects', 'is_jury', 'image',)
