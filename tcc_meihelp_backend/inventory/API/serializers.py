from rest_framework import serializers

from tcc_meihelp_backend.inventory.models import Stock, Product, Provider, StockProduct


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phone']


class ProductSerializer(serializers.ModelSerializer):
    providers = ProviderSerializer(many=True)
    category = serializers.CharField(source='category_label')

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'providers']


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
