from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Book(models.Model):
    name = models.TextField()
    author =  models.CharField(max_length=600)
    published_date = models.DateField()
    sammari = models.TextField()
    cover = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name
    
class Author(models.Model):
    firstName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    dateOfBirth = models.DateField()
    biography = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
    
