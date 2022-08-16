from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from tcc_meihelp_backend.inventory.API.serializers import StockSerializer
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
