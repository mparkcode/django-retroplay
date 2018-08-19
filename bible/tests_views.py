from django.test import TestCase

# Create your tests here.
class TestBibleViews(TestCase):
    
    def test_get_search_bible_page(self):
        page = self.client.get("/bible/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bible/search_bible.html")
        
    # def test_get_game_detail_page(self):
    #     page = self.client.get("/bible/game_detail?game_id=427")
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "bible/game_detail.html")
    
    def test_get_game_detail_page_redirect_if_no_game_id(self):
        response = self.client.get("/bible/game_detail")
        self.assertRedirects(response, '/bible/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        