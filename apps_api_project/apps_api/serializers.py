from rest_framework import serializers
from .models import Apps


class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ('id', 'title', 'description', 'api_key', 'created_date')
        read_only_fields = ('id', 'api_key', 'created_date')
