from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tcc_meihelp_backend.inventory.API.serializers import StockSerializer, ProductSerializer, ProviderSerializer, \
    StockProductSerializer
from tcc_meihelp_backend.inventory.models import Stock, StockProduct, ProviderProducts, Product, Provider


class InventoryViewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def list(self, request, *args, **kwargs):
        company = request.user
        user_stocks = [x for x in Stock.objects.filter(company_id=company.id)]

        for stock in user_stocks:
            for product in stock.products.all():
                product.quantity = StockProduct.objects.get(product_id=product.id, stock_id=stock.id).quantity

        serializer = StockSerializer(user_stocks, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')

        if not name:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        stock = {
            'name': name,
            'company': request.user,
            'created_at': datetime.now()
        }

        stock = Stock.objects.create(**stock)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        stock = self.get_object()
        name = request.data.get('name')

        if not name:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        stock.name = name
        stock.save()
        serializer = StockSerializer(stock)
        return Response(serializer.data)


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        company = self.request.user
        return Product.objects.filter(created_by=company.id)

    def create(self, request, *args, **kwargs):
        company = request.user
        name = request.data.get('name')
        description = request.data.get('description')
        providers = request.data.get('providers')
        category = request.data.get('category')

        if not name or not description or not category:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        product = {
            'name': name,
            'description': description,
            'category': category,
            'created_by': company,
        }

        product = Product.objects.create(**product)

        product.providers.set(providers)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        product = self.get_object()
        name = request.data.get('name')
        description = request.data.get('description')
        providers = request.data.get('providers')
        category = request.data.get('category')

        if name:
            product.name = name

        if description:
            product.description = description

        if providers:
            product.provider = providers

        if category:
            product.category = category

        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_provider(self, request, pk=None):
        provider_id = request.data.get('provider_id')
        product = self.get_object()
        product.providers.add(Provider.objects.get(id=provider_id))
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def remove_provider(self, request, pk=None):
        provider_id = request.data.get('provider_id')
        product = self.get_object()
        provider = Provider.objects.get(id=provider_id)
        provider_products = ProviderProducts.objects.get(product=product, provider=provider)
        provider_products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProviderViewset(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer

    def get_queryset(self):
        company = self.request.user
        return Provider.objects.filter(created_by=company.id)

    def create(self, request, *args, **kwargs):
        company = request.user
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')

        if not name or not email or not phone:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        provider = {
            'name': name,
            'email': email,
            'phone': phone,
            'created_by': company,
        }

        provider = Provider.objects.create(**provider)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)


class StockProductViewset(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def add_product(self, request):
        stock_id = request.data.get('stock_id')
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))

        if not product_id or not quantity or not stock_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        stock = Stock.objects.get(id=stock_id)
        product = Product.objects.get(id=product_id)

        try:
            stock_product = StockProduct.objects.get(stock=stock, product=product)
            stock_product.quantity += quantity
            stock_product.save()
        except StockProduct.DoesNotExist:
            stock_product = StockProduct.objects.create(stock=stock, product=product, quantity=quantity)

        serializer = StockProductSerializer(stock_product)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def decrease_product_quantity(self, request):
        stock_id = request.data.get('stock_id')
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity'))

        if not product_id or not quantity or not stock_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        stock = Stock.objects.get(id=stock_id)
        product = Product.objects.get(id=product_id)

        try:
            stock_product = StockProduct.objects.get(stock=stock, product=product)
            if stock_product.quantity - quantity < 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            stock_product.quantity -= quantity
            stock_product.save()
        except StockProduct.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = StockProductSerializer(stock_product)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def remove_product(self, request):
        stock_id = request.data.get('stock_id')
        product_id = request.data.get('product_id')

        if not product_id or not stock_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        stock = Stock.objects.get(id=stock_id)
        product = Product.objects.get(id=product_id)
        stock_product = StockProduct.objects.get(stock=stock, product=product)
        stock_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
