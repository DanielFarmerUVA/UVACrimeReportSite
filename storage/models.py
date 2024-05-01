from django.db import models

class File(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to = 'uploadedFiles/')
# Create your models here.
