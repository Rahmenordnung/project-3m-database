from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    #Ensure that flask is set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
        
    #Ensure that the login pages contains the specified words    
    def test_words_in_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)
        
    #Ensure that login behaves correctly given the correct credencials
    
    def test_login_correct(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'you&#39;re logging has been successful', response.data)
    
    
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
    
    def test_mongo_displayed(self):
        tester = app.test_client(self)
        response = tester.post('/add_recipe', data=dict(username="admins", password="adminw"), follow_redirects=True)
        self.assertIn(b'Add recipe', response.data)
    
    
     
     
    
    
    
if __name__ == '__main__':
    unittest.main()