from rest_framework import viewsets

from tcc_meihelp_backend.activities.models import Activity


class ActivityViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
