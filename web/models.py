from django.db import models
from accounts.models import Staff, Member
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Default description')
    img = models.ImageField(upload_to = 'images')
    date = models.DateField()
    
    def __str__(self):
        return self.title
    
    
class News(models.Model):
    title = models.CharField(max_length=150)
    auther = models.CharField(max_length=50)
    description = models.TextField(default='Default description')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_member': True})
    name = models.CharField(max_length=100)
    email = models.EmailField()
    level_of_education = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    phone_number = models.CharField(max_length=15)
    date_of_application = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"