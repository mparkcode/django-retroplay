from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from .models import Article, Comment
from django.contrib.auth.models import User
# Create your tests here.
class TestNewsViews(TestCase):
    
    def test_all_news_returns_301_status_code(self):
        page = self.client.get("/news/")
        self.assertEqual(page.status_code, 200)
        
    def test_get_view_article_page(self):
        article = Article(title="Example article", content="example content")
        article.save()
        page = self.client.get("/news/{0}".format(article.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "news/view_article.html")
        
    def test_search_query_redirect_on_all_news(self):
        response = self.client.get("/news/?query=sonic")
        self.assertRedirects(response, '/games/search_results/sonic', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_search_query_redirect_on_view_article(self):
        article = Article(title="Example article", content="example content")
        article.save()
        response = self.client.get("/news/{0}?query=sonic".format(article.id))
        self.assertRedirects(response, '/games/search_results/sonic', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
        
    def test_post_create_a_comment(self):
        User.objects.create_user(username='test', email='test@example.com', password='Madetotest')
        self.client.login(username='test', password='Madetotest')
        article = Article(title="Example article", content="example content")
        article.save()
        response = self.client.post("/news/{0}".format(article.id), {'content':"Example comment", 'comment_id': ""})
        comment = get_object_or_404(Comment, pk=1)
        self.assertRedirects(response, '/news/{0}'.format(article.id), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_can_edit_comment(self):
        User.objects.create_user(username='test', email='test@example.com', password='Madetotest')
        self.client.login(username='test', password='Madetotest')
        article = Article(title="Example article", content="example content")
        article.save()
        comment = Comment(content="test comment", article=article)
        comment.save()
        response = self.client.post("/news/{0}".format(article.id), {'content':"Example comment", 'comment_id': comment.id})
        self.assertRedirects(response, '/news/{0}'.format(article.id), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_can_delete_comment(self):
        User.objects.create_user(username='test', email='test@example.com', password='Madetotest')
        self.client.login(username='test', password='Madetotest')
        article = Article(title="Example article", content="example content")
        article.save()
        comment = Comment(content="test comment", article=article)
        comment.save()
        response = self.client.post("/news/{0}".format(article.id), {'comment_id': comment.id})
        self.assertRedirects(response, '/news/{0}'.format(article.id), status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_comment_content_appears_in_form_to_edit(self):
        User.objects.create_user(username='test', email='test@example.com', password='Madetotest')
        self.client.login(username='test', password='Madetotest')
        article = Article(title="Example article", content="example content")
        article.save()
        comment = Comment(content="test comment", article=article)
        comment.save()
        page = self.client.get("/news/{0}?comment_id={1}".format(article.id,comment.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "news/view_article.html")