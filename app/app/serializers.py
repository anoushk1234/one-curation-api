from rest_framework import serializers
from .models import Project, ProjectPosts


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPosts
        fields = "__all__"
