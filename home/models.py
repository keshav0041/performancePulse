from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    enrollment_no = models.CharField(max_length=50)
    cgpa = models.FloatField()
    attendance = models.FloatField()
    performance = models.FloatField()
    category = models.CharField(max_length=50)