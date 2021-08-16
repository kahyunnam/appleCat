from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import Cat, Apple
from .serializers import SecretCatSerializer, CatSerializer
import uuid

'''
for creating new accounts
'''


@api_view(['POST'])
def create_account(request):
    seriCat = SecretCatSerializer(data=request.data)
    if seriCat.is_valid():
        seriCat.save()

        new_cat = Cat.objects.get(accessKey="NEWCAT")
        new_cat.accessKey = str(uuid.uuid1())
        new_cat.save()
        new_seriCat = CatSerializer(new_cat)

        return Response(new_seriCat.data, status=status.HTTP_201_CREATED)

    return Response(seriCat.errors, status=status.HTTP_400_BAD_REQUEST)


'''
for logging in
'''


@api_view(['GET'])
def login_access(request):

    catUserName = request.data.get("userName")
    catUserPassword = request.data.get("userPassword")

    fail = {
        "login": False,
        "accessKey": ""
    }

    try:
        userCat = Cat.objects.get(userName=catUserName)
        if (userCat.userPassword == catUserPassword):
            success = {
                "login": True,
                "accessKey": userCat.accessKey
            }
            return JsonResponse(success)
        else:
            return JsonResponse(fail)

    except Cat.DoesNotExist:
        return JsonResponse(fail)
