from rest_framework import serializers

from tcc_meihelp_backend.trainings.models import Training


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'
