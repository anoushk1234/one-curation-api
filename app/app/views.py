from urllib import request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ProjectSerializer, ProjectPostsSerializer
from .models import Project, ProjectPosts


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    return Response("Help human be human😊", 200)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, 200)
