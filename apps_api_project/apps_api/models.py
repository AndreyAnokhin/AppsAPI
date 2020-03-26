from django.db import models
from rest_framework_api_key.models import APIKey


class Apps(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    api_key = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def create_api_key(self):
        api_key, key = APIKey.objects.create_key(name=self.title)
        return key

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = self.create_api_key()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
