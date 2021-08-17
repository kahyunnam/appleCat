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


class AppleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apple
        fields = (
            'cat',
            'company',
            'jobTitle',
            'location',
            'submittedDate',
            'description',
            'notes',
            'statusCheck',
            'OAStatusChoices',
            'OAstatus',
            'OAdue',
            'OAlink',
            'OAThoughtsChoices',
            'OAthoughts',
            'pending',
            'rejected',
            'accepted',
            'interviewInvite',
            'interviewDate'
        )
