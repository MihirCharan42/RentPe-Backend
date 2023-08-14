from django.shortcuts import render
from rest_framework.decorators import *
from .models import User
from django.http import JsonResponse
import json
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import AllowAny
from django.db.models import Q

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(req):
    body = json.loads(req.body.decode("utf-8"))
    try:
        name = body["name"]
        mobile = body["mobile"]
        email = body["email"]
        password = body["password"]
        try:
            user = User.objects.get(Q(mobile = mobile) | Q(email = email))
            if(user is not None):
                res = {"flag" : True, "message": "User Already Exists!"}
                return JsonResponse(res, safe= False)
        except User.DoesNotExist:
            data = User(name = name, email = email, mobile = mobile, password = password)
            data.save()
            res = {"flag" : True, "message": "User is created successfully!"}
            return JsonResponse(res, safe= False)
    except Exception as e:
        res = {"flag" : False, "message": str(e)}
        return JsonResponse(res, safe= False)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(req):
    body = json.loads(req.body.decode("UTF-8"))
    try:
        login_key = body["login_key"]
        password = body["password"]
        if '@' in login_key :
            user = User.objects.get(email = login_key)
        else :
            user = User.objects.get(mobile = login_key)
        if(password == user.password):
            refresh = RefreshToken.for_user(user)
            res = {"flag" : True, "id": user.id, "name": user.name, "mobile": user.mobile, "email": user.email, "jwt_refresh_token" : str(refresh), "jwt_access_token" : str(refresh.access_token)}
            return JsonResponse(res, safe= False)
        else:
            res = {"flag" : False, "message": "Incorrect Credentials"}
            return JsonResponse(res, safe= False)
    except User.DoesNotExist:
        res = {"flag" : False, "message": "User does Not exist"}
        return JsonResponse(res, safe= False)
    except Exception as e:
        res = {"flag" : False, "message": str(e)}
        return JsonResponse(res, safe= False, status = 500)

@api_view(['POST'])
@permission_classes([AllowAny])
def new_access_token(req):
    body = json.loads(req.body.decode("UTF-8"))
    try:
        refresh_token = body["jwt_refresh_token"]
        new_token = RefreshToken(refresh_token)
        res = {"flag" : True, "jwt_access_token": str(new_token.access_token)}
        return JsonResponse(res, safe=False)
    except Exception as e:
        res = {"flag" : False, "message": str(e)}
        return JsonResponse(res, safe=False)