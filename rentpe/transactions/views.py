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
from datetime import datetime

# Create your views here.

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
def create_transaction(req):
    body = json.loads(req.body.decode("UTF-8"))
    try:
        home_id = body["home_id"]
        amount = body["amount"]
        transaction_id = body["transaction_id"]

        try:
            home = Home.objects.get(id = home_id)
            tenant_user = home.tenant_user
            landlord_user = home.landlord_user

            home.last_payment = datetime.today()
            home.rent_due = datetime.today().replace(month=datetime.today().month+1)
            home.save()

            data = Transaction(home = home, tenant_user = tenant_user, landlord_user = landlord_user, amount = amount, transaction_id = transaction_id)
            data.save()
            res = {"flag": True, "message": "Transaction has been created"}
            return JsonResponse(res, safe= False, status = 200)
        except Home.DoesNotExist:
            res = {"flag": False, "message": "Home with this id does not exists."}
            return JsonResponse(res, safe= False, status = 200)
        except Exception as e:
            res = {"flag": False, "message": str(e)}
            return JsonResponse(res, safe= False, status = 200)
    except Exception as e:
            res = {"flag": False, "message": str(e)}
            return JsonResponse(res, safe= False, status = 200)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def read_transaction(req):
    user = req.user
    try:
        transactions = Transaction.objects.filter(Q(landlord_user=user) | Q(tenant_user=user)).values(
            "landlord_user__name", 
            "tenant_user__name", 
            "amount",
            "transaction_id")
        data = list(transactions)
        if len(data) == 0 :
            res ={"flag": False, "message": "No transactions were created"}
        else:
            res ={"flag": True, "results": data}
        return JsonResponse(res, safe= False, status=200)
    except Home.DoesNotExist :
        res = {"flag": False, "message": "No homes were found"}
        return JsonResponse(res, safe= False, status=200)  
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