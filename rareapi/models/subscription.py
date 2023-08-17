from django.db import models

class Subscription(models.Model):
    follower = models.ForeignKey("RareUser", on_delete=models.DO_NOTHING, related_name='subscription_follower')
    author =   models.ForeignKey("RareUser", on_delete=models.DO_NOTHING, related_name = 'followed_by')
    created_on = models.DateField(auto_now_add=True)
    ended_on = models.DateField(auto_now_add=False, default= None, null=True, blank=True)

