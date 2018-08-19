from django.test import TestCase
import os
from igdb_api_python.igdb import igdb
# Create your tests here.
class TestBibleViews(TestCase):
    
    def test_get_search_bible_page(self):
        page = self.client.get("/bible/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bible/search_bible.html")
        
    
    
    def test_get_game_detail_page_redirect_if_no_game_id(self):
        response = self.client.get("/bible/game_detail")
        self.assertRedirects(response, '/bible/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_search_query_redirect_on_get_games(self):
        response = self.client.get("/bible/?query=test")
        self.assertRedirects(response, '/games/search_results/test', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_search_query_redirect_on_game_detail_page(self):
        response = self.client.get("/bible/game_detail?game_id=427&query=test")
        self.assertRedirects(response, '/games/search_results/test', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_result_of_igdb_search_in_game_detail(self):
        r = igdb(os.environ.get("IGDB_API_KEY"))
        response = self.client.get("/bible/game_detail?game_id=427")
        result = r.games({
            'search': "427"
        })
        assert result.body != []
        
    def test_result_of_igdb_search_in_get_games(self):
        r = igdb(os.environ.get("IGDB_API_KEY"))
        response = self.client.get("/bible/?igdb_search=test")
        result = r.games({
            'search': "427"
        })
        assert result.body != []
        
