from rest_framework import viewsets
from .models import Course
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import CourseSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #need to be user to have access to course objects 
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )









