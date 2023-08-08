import jwt
from rest_framework.authentication import BaseAuthentication
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
from authentication.models import User


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        return reason

class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        authorization_heaader = request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        try:
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None)
