from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import EstateSerializerz, StatusSerializers, BelongingSerializers, UserSerializer, CommentSerializer
from django.apps import apps
from django.contrib.auth.models import User
model = apps.get_model('estate', 'status')
model2 = apps.get_model('estate', 'belongings')
model4 = apps.get_model('estate', 'Estate')
model3 = apps.get_model('users', 'Profile')
model5 = apps.get_model('estate', 'comment')


# Create your views here.
class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = model.objects.all()
    serializer_class = StatusSerializers
    permission_classes = []


class BelongingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = model2.objects.all()
    serializer_class = BelongingSerializers
    permission_classes = []


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

class EstateViewSet(viewsets.ModelViewSet):
    queryset = model4.objects.all()
    serializer_class = EstateSerializerz
    permission_classes = []

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = model5.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []
