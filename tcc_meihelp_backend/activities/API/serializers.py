from rest_framework import serializers

from tcc_meihelp_backend.activities.models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
