from app import app
import unittest
import mock

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client(self)
        
    ###############
    #### test views ####
    ###############
    
    #Ensure that flask is set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
     #Ensure that add_recipe worked up correctly, and contains some text in the title
        
    def test_add_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/add_recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/edit_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_update_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/update_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_delete_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/delete_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_see_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/see_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
        
    def test_get_cuisine(self):
        tester = app.test_client(self)
        response = tester.get('/get_cuisine', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_edit_cuisine(self):
        tester = app.test_client(self)
        response = tester.get('edit_cuisine', content_type='html/text')
        self.assertEqual(response.status_code, 200) 
        
    def test_update_cuisine(self):
        tester = app.test_client(self)
        response = tester.get('/update_cuisine', content_type='html/text')
        self.assertEqual(response.status_code, 200) 
        
    def test_delete_cuisine(self):
        tester = app.test_client(self)
        response = tester.get('/delete_cuisine', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
        
    def test_new_cuisine(self):
        tester = app.test_client(self)
        response = tester.get('/new_cuisine', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_upvote_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/upvote_recipe', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    ###----------------------------###
    #### test content of views ####
    ##################################    
        
        
    #Ensure that the login pages contains the specified words    
    def test_words_in_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)
        
    def test_get_tasks(self):
        tester = app.test_client(self)
        response = tester.get('/get_tasks', content_type='html/text')
        self.assertTrue(b'Recipes' in response.data)
        self.assertTrue(b'Isombe' in response.data)
        self.assertTrue(b'Edit' in response.data)
        
    def test_add_recipes(self):
        tester = app.test_client(self)
        response = tester.get('/add_recipes', content_type='html/text')
        self.assertTrue(b'Recipe' in response.data)
        self.assertTrue(b'Cuisine' in response.data)
        
        
        
        
        
    #Ensure that login behaves correctly given the correct credencials
    
    def test_login_correct(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'you&#39;re logging has been successful', response.data)
        
    def test_edit_recipes(self):
        tester = app.test_client(self)
        response = tester.post('edit_recipes', follow_redirects=True)
        self.assertIn(b'Edit Recipe', response.data)    
    
    
    #Ensure that login behaves correctly given the incorrect credencials
    
    
    def test_login_incorrect(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admins", password="adminw"), follow_redirects=True)
        self.assertIn(b'Invalid Credentials. Please try again', response.data)
    
    
    #Ensure that logout behaves correctly
    
    #NOT WORKING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
   # def test_logout_correct(self):
    #    tester = app.test_client(self)
      #  tester.post('/login', data=dict(username="admins", password="adminw"), follow_redirects=True)
    #    response = tester.get('/get_tasks', follow_redirects= True) 
     #   self.assertIn(b'you\'re now logged out', response.data)
     
     #Ensure that login is required
     
    #def test_main_route_requires_login(self):
     #   tester = app.test_client(self)
      #  response = tester.get('/', follow_redirects=True)
       # self.assertTrue(b'Please log in first!!!' in response.data)
        
    #Ensure that logout is required
    
    #def test_main_route_requires_logout(self):
     #   tester = app.test_client(self)
      #  response = tester.get('/', follow_redirects=True)
       # self.assertTrue(b'Please log in first!!!' in response.data)
       
    #ensure display mongo db
    
   # def test_mongo_displayed(self):
    #    tester = app.test_client(self)
     #   response = tester.post('/add_recipe', data=dict(username="admin", password="admin"), follow_redirects=True)
      #  self.assertIn(b'Add recipe', response.data)
        
    def test_index_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        

    # @mock.patch('requests.post', side_effect=mock_post)
    @mock.patch('app.get_tasks')
    def test_search_box_route(self, mock_get_tasks):
        mock_get_tasks.return_value = {
            'result': []
        }
        search_term = 'text'
        response = self.app.post(
            '/search_box',
            data=dict(search_text=search_term))
        self.assertEqual(response.status_code, 308)

        response = self.app.post(
            '/search_results',
            data=dict(search_text=search_term))
        self.assertEqual(response.status_code, 302)
        response = self.app.get(
            '/get_tasks',
            data=dict(search_text=search_term))
        
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()