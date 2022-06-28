from rest_framework import serializers

from tcc_meihelp_backend.taxes.models import DAS


class DasSerializer(serializers.ModelSerializer):
    class Meta:
        model = DAS
        fields = '__all__'
