from rest_framework import serializers

from tcc_meihelp_backend.inventory.models import Stock, Product, Provider, StockProduct


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    providers = ProviderSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class StockProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity']


class StockSerializer(serializers.ModelSerializer):
    stock_products = StockProductSerializer(many=True, source='stockproduct_set')

    class Meta:
        model = Stock
        fields = ['id', 'name', 'stock_products']
