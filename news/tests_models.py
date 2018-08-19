from django.test import TestCase
from .models import Article, Comment
from django.utils import timezone
from django.contrib.auth.models import User
# Create your tests here.

class Test_News_Model(TestCase):
    
    def test_ArticleModel(self):
        p_date = timezone.now()
        article=Article(title="Example Article", content="Example Content", published_date=p_date)
        article.save()
        self.assertEqual(article.title, "Example Article")
        self.assertEqual(article.content, "Example Content")
        self.assertEqual(article.published_date, p_date)
        
    def test_article_as_string(self):
        article=Article(title="News Article")
        self.assertEqual("News Article", str(article))
        
    def test_Comment_Model(self):
        p_date = timezone.now()
        article=Article(title="Example Article", content="Example Content", published_date=p_date)
        article.save()
        comment=Comment(content="Example Comment", date=p_date, article = article)
        comment.save()
        self.assertEqual(comment.content, "Example Comment")
        self.assertEqual(comment.date, p_date)
        
    def test_comment_as_string(self):
        comment=Comment(content="Comment")
        self.assertEqual("Comment", str(comment))