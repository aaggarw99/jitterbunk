from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photo = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Bunk(models.Model):
    from_user = models.OneToOneField(UserProfile, related_name="from_user")
    to_user = models.OneToOneField(UserProfile, related_name="to_user")
    timestamp = models.DateTimeField('bunking date')

    def __str__(self):
        return self.from_user.user.first_name + " --> " + self.to_user.user.first_name + " @ " + str(self.timestamp)


    
