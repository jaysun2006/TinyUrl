from django.conf import settings
from django.db import models


class URL(models.Model):
    tiny_url = models.CharField(max_length=256, unique=True, blank=True)
    source_url = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tiny_url

    def get_url_data(self):
        return settings.DOMAIN_URL + self.tiny_url
