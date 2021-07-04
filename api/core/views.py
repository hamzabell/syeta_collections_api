from .permissions import ViewPermissions
from django.conf import settings
from .authentication import JWTAuthentication
from rest_framework.serializers import Serializer
from .models import Company, Permission, Role, User
from rest_framework.views import APIView
from .serializers import CompanySerializer, LoginSerializer, PermissionSerializer, RoleSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import exceptions, generics
from rest_framework.permissions import IsAuthenticated
import jwt

# Create your views here.
class PermissionAPIView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    permission_object ="permissions"

class RoleAPIView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CompanyAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated  & ViewPermissions]
    authentication_classes = [JWTAuthentication]

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated & ViewPermissions]
    authentication_classes = [JWTAuthentication]
    permission_object = "users"

    def post(self, request, format=None):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    def get(self, request, pk=None, format=None):
        if pk is None:
            serializer = UserSerializer(User.objects.all(), many=True)
            return Response(serializer.data)
        
        data = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(data)
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(email=serializer.data.get('email')).first()

        if not user:
            raise exceptions.AuthenticationFailed('User not Found')

        if not user.check_password(serializer.data.get('password')):
            raise exceptions.AuthenticationFailed('Password not Correct')

        response = Response()


        response.data = {
            "message": "success",
            'access': JWTAuthentication.generate_access_token(user),
            'refresh': JWTAuthentication.generate_refresh_token(user)
        }

        return response

class RefreshTokenAPIView(APIView):
    def post(self, request):
        token = request.data['token']
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, 'HS256')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token Expired. Please re-login')

        if payload['type'] != 'refresh':
            raise exceptions.AuthenticationFailed('Please pass the refresh token')

        user = User.objects.get(pk=payload['user_id'])

        if not user:
            raise exceptions.AuthenticationFailed('User not Found')

        response = Response()

        response.data = {
            "message": "success",
            'access': JWTAuthentication.generate_access_token(user),
        }

        return response
    

        
