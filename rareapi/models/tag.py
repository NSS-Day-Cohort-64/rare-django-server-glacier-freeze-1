from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=55)
    posts = models.ManyToManyField("Post", through = "PostTag")
