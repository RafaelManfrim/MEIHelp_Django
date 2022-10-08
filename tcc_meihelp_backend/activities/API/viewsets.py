from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response

from tcc_meihelp_backend.activities.API.serializers import ActivitySerializer
from tcc_meihelp_backend.activities.models import Activity


class ActivityViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def list(self, request, *args, **kwargs):
        activity = Activity.objects.filter(company=request.user)
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        forecast_date = request.data.get('forecast_date')

        if not title or not forecast_date:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        company = request.user

        data = {
            'title': title,
            'description': description,
            'forecast_date': forecast_date,
            'finished': False,
            'company': company,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
        }

        activity = Activity(**data)

        activity.save()

        serializer = ActivitySerializer(activity)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        activity = self.get_object()

        if activity.company_id != request.user.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if activity.finished:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        title = request.data.get('title')
        description = request.data.get('description')
        forecast_date = request.data.get('forecast_date')

        if not title or not forecast_date:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        activity.title = title
        activity.description = description
        activity.forecast_date = forecast_date
        activity.updated_at = datetime.now()
        activity.save()

        serializer = ActivitySerializer(activity)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        activity = self.get_object()

        if activity.company_id != request.user.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if activity.finished:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        activity.finished = True
        activity.updated_at = datetime.now()
        activity.finished_at = datetime.now()
        activity.save()

        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        activity = self.get_object()

        if activity.company_id != request.user.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
