from django.db import models

class RareUser(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING, related_name='rare_user_info')
    bio = models.CharField(max_length=55)
    profile_image_url = models.CharField(max_length=400)
    created_on = models.DateField(auto_now=True, auto_now_add=True)
    active = models.BigIntegerField(default=True)

