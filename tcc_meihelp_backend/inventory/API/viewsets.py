from rest_framework import viewsets
from rest_framework.response import Response

from tcc_meihelp_backend.inventory.API.serializers import StockSerializer
from tcc_meihelp_backend.inventory.models import Stock, StockProduct, ProviderProducts, Product, Provider


class InventoryViewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def list(self, request):
        company = request.user
        user_stocks = Stock.objects.filter(company_id=company.id)

        # stocks = []
        #
        # for stock in user_stocks:
        #     stock_products = StockProduct.objects.filter(stock=stock)
        #     products = []
        #     for stock_product in stock_products:
        #         product = Product.objects.get(id=stock_product.product.id)
        #         product_providers = ProviderProducts.objects.filter(product=product)
        #         products.append({
        #             'product': product,
        #             'providers': product_providers
        #         })
        #
        #     stocks.append({
        #         'stock': stock,
        #         'products': products
        #     })
        #
        # print(stocks)

        serializer = StockSerializer(user_stocks, many=True)
        return Response(serializer.data)
