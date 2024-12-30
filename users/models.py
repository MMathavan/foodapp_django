from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   #means that if the user is deleted the profile of the user is also be deleted...
    image = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')  #in this it will take profilepic.jpg as default profile image for all new users..
    location = models.CharField(max_length=100)

    def __str__(self):            #it is used to create objects for this model
        return f'{self.user.username}'
    