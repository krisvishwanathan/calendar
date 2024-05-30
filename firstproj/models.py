from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_phone = models.CharField(max_length=20, null=True, blank=True)
    client_address = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "tblevents"  