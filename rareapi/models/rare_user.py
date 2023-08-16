from django.db import models
from django.contrib.auth.models import User


class RareUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    bio = models.CharField(max_length=55)
    profile_image_url = models.CharField(max_length=14000)
    created_on = models.DateField(auto_now_add=True)
    active = models.BigIntegerField(default=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
