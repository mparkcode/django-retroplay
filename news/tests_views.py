from django.test import TestCase
from .models import Article

# Create your tests here.
class TestNewsViews(TestCase):
    
    def test_all_news_returns_301_status_code(self):
        page = self.client.get("/news")
        self.assertEqual(page.status_code, 301)
        
    def test_get_view_article_page(self):
        article = Article(title="Example article", content="example content")
        article.save()
        page = self.client.get("/news/{0}".format(article.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "news/view_article.html")