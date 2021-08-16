from rest_framework import serializers
from .models import Cat, Apple


class SecretCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('userName', 'userPassword', 'accessKey')

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('userName', 'userPassword')
