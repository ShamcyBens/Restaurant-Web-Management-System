from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, default='example@gmail.com')
    avatar = models.ImageField(default='static/profile_pics/default.png', upload_to='static/profile_pics')
    bio = models.TextField(max_length=400)

    def __str__(self):
        return f'{self.user.username} Profile'



# class Room(models.Model):
#     room_name = models.CharField(max_length=100)
#     room_capacity = models.PositiveIntegerField()
#     room_pricing = models.IntegerField()
