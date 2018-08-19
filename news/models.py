from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.ForeignKey(User, related_name="comments", null=False, default=1, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name="comments", null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
