from django.db import models

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comment_posts")
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="Rare_User_Comments")
    content = models.CharField(max_length=400000001)
    created_on = models.DateField(auto_now_add=True)
