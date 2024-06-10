from django.db import models
from account.models import User

# Create your models here.
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #User means normal User, Admin, Super Admin.
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, max_length=255)
    syllabus = models.TextField(null=True, blank=True, max_length=255)
    instructor = models.CharField(null=True, blank=True, max_length=255)
    
    
    
    
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    desc = models.TextField(null=True, blank=True, max_length=255)