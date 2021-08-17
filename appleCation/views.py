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
from .serializers import SecretCatSerializer, CatSerializer, AppleSerializer
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
        new_seriCat = SecretCatSerializer(new_cat)

        return Response(new_seriCat.data, status=status.HTTP_201_CREATED)

    fail = {
        "userName": "notvalid",
        "userPassword": "notvalid",
        "accessKey": "notvalid"
    }
    return JsonResponse(fail)


'''
for logging in
'''


@api_view(['POST'])
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
                "id": userCat.id,
                "login": True,
                "accessKey": userCat.accessKey
            }
            return JsonResponse(success)
        else:
            return JsonResponse(fail)

    except Cat.DoesNotExist:
        return JsonResponse(fail)


'''
creating job application

required data fields: cat(model), company(char), jobtitle(char), location(char), submittedDate(char)

optional: pending(bool), rejected(bool), accepted(bool), description(text), notes(text)
'''


@api_view(['POST'])
def new_apple(request):
    seriApple = AppleSerializer(data=request.data)
    if seriApple.is_valid():
        seriApple.save()
        return Response(seriApple.data, status=status.HTTP_201_CREATED)

    fail = {
        "cat": "fieldsnotvalid"
    }
    return Response(seriApple.errors)
    # return JsonResponse(fail)


'''
update job application
'''


@api_view(['PUT'])
def update_apple(request, accessKey, id):
    try:
        Cat.objects.get(accessKey=accessKey)
        try:
            theApple = Apple.objects.get(id=id)
            newSeriApple = AppleSerializer(data=request.data)
            if newSeriApple.is_valid():

                # probs a better way to do this but whatever
                theApple.company = request.data.get("company")
                theApple.jobTitle = request.data.get("jobTitle")
                theApple.location = request.data.get("jobTitle")
                theApple.submittedDate = request.data.get("submittedDate")
                theApple.pending = request.data.get("pending")
                theApple.rejected = request.data.get("rejected")
                theApple.accepted = request.data.get("accepted")
                theApple.description = request.data.get("description")
                theApple.notes = request.data.get("notes")

                theSeriApple = AppleSerializer(theApple)
                return Response(theSeriApple.data)

            fail = {
                "cat": "fieldsnotvalid"
            }
            return JsonResponse(fail)

        except Apple.DoesNotExist:
            fail = {
                "cat": "appledoesnotexist"
            }
            return JsonResponse(fail)

    except Cat.DoesNotExist:
        fail = {
            "cat": "catdoesnotexist"
        }
        return JsonResponse(fail)
