from django.test import TestCase
from .models import Article, Comment
from django.utils import timezone
from django.contrib.auth.models import User
# Create your tests here.

class TestNewsModel(TestCase):
    
    def testArticleModel(self):
        p_date = timezone.now()
        article=Article(title="Example Article", content="Example Content", published_date=p_date)
        article.save()
        self.assertEqual(article.title, "Example Article")
        self.assertEqual(article.content, "Example Content")
        self.assertEqual(article.published_date, p_date)
        
    def testCommentModel(self):
        p_date = timezone.now()
        article=Article(title="Example Article", content="Example Content", published_date=p_date)
        article.save()
        comment=Comment(content="Example Comment", date=p_date, article = article)
        comment.save()
        self.assertEqual(comment.content, "Example Comment")
        self.assertEqual(comment.date, p_date)