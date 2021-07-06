from django.db.models import query
from core.serializers import CompanySerializer
from core.models import Company
from rest_framework import serializers
from .models import Product


class CompanyRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return CompanySerializer(value).data
    def to_internal_value(self, data):
        return self.queryset.get(pk=data)

    
class ProductSerializer(serializers.ModelSerializer):
    company = CompanyRelatedField(many=False, queryset=Company.objects.all())
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'company']
        extra_kwargs = {
            'company': { 'required': True }
        }