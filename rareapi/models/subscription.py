from django.db import models

class Subscription(models.Model):
    follower = models.ForeignKey("Rare_User", on_delete=models.DO_NOTHING, related_name='subscription_follower')
    author =   models.ForeignKey("Rare_User", on_delete=models.DO_NOTHING, related_name = 'followed_by')
    created_on = models.DateField(auto_now=True, auto_now_add=True)
    ended_on = models.DateField(auto_now=True, auto_now_add=True)

