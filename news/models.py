from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_articles')
    
    def __str__(self):
        return self.title
