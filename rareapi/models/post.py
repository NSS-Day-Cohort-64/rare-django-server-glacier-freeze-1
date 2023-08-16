from django.db import models

class Post(models.Model):
    user = models.ForeignKey("RareUser", on_delete=models.DO_NOTHING, related_name="rare_user_posts")
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING, related_name="category_posts")
    title = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now_add=True)
    image_url = models.CharField(max_length=500)
    content = models.CharField(max_length=5000)
    approved = models.BooleanField(default=True)

