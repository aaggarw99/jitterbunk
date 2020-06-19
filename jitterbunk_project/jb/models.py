from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    """
    UserProfile Object
    - USER points to the auth.User object of a user
    - PHOTO holds a link to a user's photo.
    """
    user = models.OneToOneField(User)
    photo = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Bunk(models.Model):
    """
    Bunk Object
    - FROM_USER, TO_USER fields to denote which users sent a bunk
    - TIMESTAMP field denoting the time of when the bunk was sent
    """
    # related_name denotes the relationship from User to UserProfile
    # TODO: foreign key fields instead
    from_user = models.ForeignKey(UserProfile, related_name="bunk_received")
    to_user = models.ForeignKey(UserProfile, related_name="bunk_sent")

    # auto_now defaults the time to now
    timestamp = models.DateTimeField('bunking date', auto_now=True)

    def __str__(self):
        return self.from_user.user.first_name + " --> " + self.to_user.user.first_name + " @ " + str(self.timestamp)


    
