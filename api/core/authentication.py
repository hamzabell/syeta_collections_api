from .models import User
from datetime import datetime, timedelta

from rest_framework import exceptions
import jwt
from rest_framework.authentication import BaseAuthentication
from django.conf import settings

class JWTAuthentication(BaseAuthentication):
    @staticmethod
    def generate_access_token(user):
        access_token_payload = {
            "type": "access",
            "user_id": user.id,
            "exp": (datetime.utcnow() + timedelta(minutes=15)).timestamp(),
            "int": datetime.utcnow().timestamp()
        }

        return jwt.encode(access_token_payload, settings.SECRET_KEY, 'HS256')

    @staticmethod
    def generate_refresh_token(user):
        refresh_token_payload = {
            "type": "refresh",
            "user_id": user.id,
            "exp": (datetime.utcnow() + timedelta(days=1)).timestamp(),
            "int": datetime.utcnow().timestamp()
        }

        return jwt.encode(refresh_token_payload, settings.SECRET_KEY, 'HS256')

    def authenticate(self, request):
        headers = request.headers.get('Authorization')

        if not headers:
            raise exceptions.AuthenticationFailed('Please povide Authorization Header')
            
        token  = headers.split(" ")[1]

        if not token:
            raise exceptions.AuthenticationFailed('Please provide a token in the Authorization Header')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, 'HS256')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Access token has expired')

        if payload['type'] != 'access':
            raise exceptions.AuthenticationFailed('Please provide the access token')

        user = User.objects.get(pk=payload['user_id'])

        if not user:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None)
