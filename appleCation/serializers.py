from rest_framework import serializers
from .models import Cat, Apple, AppleOA, AppleInterview


class SecretCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'userName', 'userPassword', 'accessKey')


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('userName', 'userPassword')


class AppleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apple
        fields = (
            'id',
            'cat',
            'company',
            'jobTitle',
            'location',
            'submittedDate',
            'pending',
            'rejected',
            'accepted',
            'description',
            'notes',
        )


class AppleOASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppleOA
        fields = (
            'apple',
            'OAName',
            'OADue',
            'OALink',
            'OAStatus',
            'OARef'
        )


class AppleInterviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppleInterview
        fields = (
            'apple',
            'interviewName',
            'interviewDate',
            'interviewLink',
            'interviewStatus',
            'interviewRef'
        )
