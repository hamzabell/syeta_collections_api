from rest_framework import serializers
from .models import Company, Permission, Role, User


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Permission.objects.all())

    class Meta:
        model = Role
        fields = '__all__'

class CompanyRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return CompanySerializer(value).data
    def to_internal_value(self, data):
        return self.queryset.get(pk=data)

class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return RoleSerializer(value).data
    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class UserSerializer(serializers.ModelSerializer):
    company = CompanyRelatedField(many=False, queryset=Company.objects.all())
    role = RoleRelatedField(many=False, queryset=Role.objects.all())
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role', 'company', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
