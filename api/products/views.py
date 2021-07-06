from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product
from core.permissions import ViewPermissions
from core.authentication import JWTAuthentication
from rest_framework import generics, mixins, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class ProductAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated & ViewPermissions]
    permission_object ="products"
    
    def get_company_id(self, request):
        return request.user.company.id

    def get(self, request, pk=None):
        company_id = self.get_company_id(request=request)
        if pk:
            products = Product.objects.filter(id=pk, company=company_id).first()
        else:
            products = Product.objects.filter(company=company_id).all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        company_id = self.get_company_id(request=request)
        data = request.data
        data['company'] = company_id

        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        company_id = self.get_company_id(request=request)
        data = request.data

        if not data:
            raise exceptions.APIException('Please pass some data to be updated')

        product  = Product.objects.filter(company=company_id, pk=pk).first()

        if not product:
            raise exceptions.APIException('Product does not exist')

        serializer = ProductSerializer(instance=product, data=data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk=None, format=None):
        company_id = self.get_company_id(request=request)
        product = Product.objects.filter(company=company_id, pk=pk)

        if not product:
            raise exceptions.APIException('Product does not exist')
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



