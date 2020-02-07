from django.test import TestCase
from .views import confirmLogin, user_signUp, user_login
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class UserTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)


    def test_signup_page_url(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
   
    def test_user_count(self):
        user = User.objects.all()
        self.assertEqual(user.count(), 1)

    def test_authentication(self):
     user = authenticate(username='testuser', password='secret')
     self.assertTrue((user is not None) and user.is_authenticated)