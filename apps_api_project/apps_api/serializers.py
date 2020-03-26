from rest_framework import serializers
from .models import Apps


class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ('id', 'title', 'description', 'api_key')
        read_only_fields = ('api_key',)
