from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Apps
from .serializers import AppsSerializer


class AppsView(ListCreateAPIView):
    queryset = Apps.objects.all()
    serializer_class = AppsSerializer


class SingleAppView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'title'
    queryset = Apps.objects.all()
    serializer_class = AppsSerializer
