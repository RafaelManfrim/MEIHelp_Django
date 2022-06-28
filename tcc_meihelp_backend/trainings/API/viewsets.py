from datetime import datetime

from rest_framework.response import Response
from rest_framework import viewsets, status

from tcc_meihelp_backend.trainings.API.serializers import TrainingSerializer
from tcc_meihelp_backend.trainings.models import Training


class TrainingViewset(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

    # def list(self, request, *args, **kwargs):

    def create(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        url = request.data.get('url')

        if not title or not url:
            return Response({'erro': 'Os campos title e url são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'title': title,
            'description': description,
            'url': url,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }

        training = Training(**data)

        training.save()

        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        training = self.get_object()

        title = request.data.get('title')
        description = request.data.get('description')
        url = request.data.get('url')

        if not title and not url and not description:
            return Response({'erro': 'É preciso alterar pelo menos um valor'}, status=status.HTTP_400_BAD_REQUEST)

        if title:
            training.title = title

        if description:
            training.description = description

        if url:
            training.url = url

        training.updated_at = datetime.now()
        training.save()

        return Response(status=status.HTTP_200_OK)

    # def destroy(self, request, *args, **kwargs)
