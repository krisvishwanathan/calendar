from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    agent_name = models.CharField(max_length=100)
    agent_type = models.CharField(max_length=50, choices=[
        ('Inbound', 'Inbound voice agent'),
        ('Outbound', 'Outbound voice agent'),
        ('Batch', 'Batch caller agent'),
    ])
    phone_number = models.CharField(max_length=20)
    csv_file = models.FileField(upload_to='csv_files/')
    first_sentence = models.CharField(max_length=20)
    business_info = models.TextField(max_length=200)

    def __str__(self):
        return self.agent_name

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