from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from django.apps import apps
model = apps.get_model('estate', 'Status')
model2 = apps.get_model('estate', 'Belongings')
model3 = apps.get_model('estate', 'Estate')
model5 = apps.get_model('estate', 'Comment')


class StatusSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = model
        fields = ['statusID', 'user', 'belonging', 'alternatives', 'rating']

class BelongingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = model2
        fields = ['name', 'description', 'estate', 'image']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class EstateSerializerz(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = model3
        fields = ['name', 'description', 'address', 'users']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = model5
        fields = ['belonging', 'user', 'body', 'created_on']
