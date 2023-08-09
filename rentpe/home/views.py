from django.shortcuts import render
from rest_framework.decorators import *
from django.http import JsonResponse
import json
from http import HTTPStatus
from django.core import serializers
from .models import *
from .verify import JWTAuthentication
from rest_framework.permissions import *
from authentication.models import User
from django.db.models import Q
import datetime
from rest_framework.permissions import IsAuthenticated
from cloudinary.uploader import upload

# Create your views here.

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
def create_home(req):

    try:
        address = req.POST.get("address")
        description = req.POST.get("description")

        tenant_name =req.POST.get("tenant_name")
        tenant_phone =req.POST.get("tenant_phone")

        landlord_name =req.POST.get("landlord_name")
        landlord_phone =req.POST.get("landlord_phone")

        rent =req.POST.get("rent")

        images = req.FILES.getlist("images")

        tenant_user = give_tenant_user(phone_number=tenant_phone)

        if(tenant_user == "Not Found" or tenant_user == Exception):
            res = {"flag": False, "message": "tenant function error"}
            return JsonResponse(res, safe= False, status = 500)
        
        landlord_user = give_landlord_user(phone_number=landlord_phone)
        
        if(landlord_user == "Not Found"  or landlord_user == Exception):
            res = {"flag": False, "message": "landlord function error"}
            return JsonResponse(res, safe= False, status = 500)
        
        public_ids = []
        for image in images:
                response = upload(image)
                print(response)
                public_ids.append(response['url'])

            
        data = Home(address = address, 
                    description = description, 
                    tenant_name = tenant_name, 
                    tenant_phone = tenant_phone,
                    landlord_name = landlord_name,
                    landlord_phone = landlord_phone,
                    rent = rent,
                    tenant_user = tenant_user,
                    landlord_user = landlord_user,
                    images = public_ids)
        data.save()
        res = {"flag": True, "message": "Home has been created"}
        return JsonResponse(res, safe= False, status = 200)
    except Exception as e:
        print(str(e))
        res = {"flag": False, "message": str(e)}
        return JsonResponse(res, safe= False, status=500)
    
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
def update_home(req):
    body = json.loads(req.body.decode("UTF-8"))
    try:
        home_id = body["home_id"]
        address = body["address"]
        description = body["description"]

        tenant_name = body["tenant_name"]
        tenant_phone = body["tenant_phone"]

        landlord_name = body["landlord_name"]
        landlord_phone = body["landlord_phone"]

        rent = body["rent"]

        tenant_user = give_tenant_user(phone_number=tenant_phone)

        if(tenant_user == "Not Found" or tenant_user == Exception):
            res = {"flag": False, "message": "tenant function error"}
            return JsonResponse(res, safe= False, status = 500)
        
        landlord_user = give_landlord_user(phone_number=landlord_phone)
        
        if(landlord_user == "Not Found"  or landlord_user == Exception):
            res = {"flag": False, "message": "landlord function error"}
            return JsonResponse(res, safe= False, status = 500)
            
        home = Home.objects.get(id = home_id)

        home.address = address
        home.description = description
        
        home.tenant_name = tenant_name
        home.tenant_user = tenant_user
        home.tenant_phone = tenant_phone

        home.landlord_name = landlord_name
        home.landlord_user = landlord_user
        home.landlord_phone = landlord_phone

        home.rent = rent
        home.updated_at = datetime.datetime.now()
        home.save()
        res = {"flag": True, "message": "Home has been created"}
        return JsonResponse(res, safe= False, status = 200)
    except Exception as e:
        print(str(e))
        res = {"flag": False, "message": str(e)}
        return JsonResponse(res, safe= False, status=500)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def read_home(req):
    user = req.user
    try:
        homes = Home.objects.filter(Q(landlord_user=user) | Q(tenant_user=user)).values(
            "id",
            "address", 
            "description", 
            "tenant_name", 
            "tenant_phone", 
            "landlord_name",
            "landlord_phone", 
            "created_at", 
            "updated_at",
            "rent")
        data = list(homes)
        if len(data) == 0 :
            res ={"flag": False, "message": "No homes were created"}
        else:
            res ={"flag": True, "results": data}
        return JsonResponse(res, safe= False, status=200)
    except Home.DoesNotExist :
        res = {"flag": False, "message": "No homes were found"}
        return JsonResponse(res, safe= False, status=500)  
    except Exception as e:
        res = {"flag": False, "message": str(e)}
        return JsonResponse(res, safe= False, status=500) 
    
def give_tenant_user(phone_number):
    try:
        tenant_user = User.objects.get(mobile = phone_number)
        return tenant_user
    except User.DoesNotExist:
        return "Not Found"
    except Exception as e:
        return e

def give_landlord_user(phone_number):
    try:
        landlord_user = User.objects.get(mobile = phone_number)
        return landlord_user
    except User.DoesNotExist:
        return "Not Found"
    except Exception as e:
        return e