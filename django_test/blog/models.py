from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) #Maxiumu length of title, makes it a character
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #This is for the access to the database, allows for a one- to many relationship
                                                            #One author, can have many posts.
    def __str__(self):
        return self.title