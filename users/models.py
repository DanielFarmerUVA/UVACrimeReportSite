from django.db import models
from datetime import datetime

class File(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to = 'uploadedFiles/')
# Create your models here.

class Report(models.Model):
    lastName = models.CharField(max_length=100, blank=True)
    firstName = models.CharField(max_length=100, blank=True)
    email = models.EmailField(null=True, blank=True)
    crimeType = models.CharField(max_length=100, choices=[
        ('Larceny/Theft', 'Larceny/Theft'),
        ('Vandalism', 'Vandalism'),
        ('Assault', 'Assault'),
        ('Harassing Phone Calls', 'Harassing Phone Calls'),
        ('Computer Harassment', 'Computer Harassment'),
        ('Narcotics/Drugs', 'Narcotics/Drugs'),
    ],     default='Larceny/Theft') 

    subject = models.CharField(max_length=255, default="No Subject")
    timeOfIncident = models.DateTimeField(default=datetime.now)
    reportDescription = models.TextField()
    descriptionItems = models.TextField(blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    discussion = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], blank=True)



    file = models.FileField(upload_to='reports/', blank=True, null=True)
    status = models.CharField(max_length=50, default='New')  # Add this line to define the 'status' field
    notes = models.TextField(blank=True)

