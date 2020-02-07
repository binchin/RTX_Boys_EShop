from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from .views import confirmLogin, user_signUp, user_login
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

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
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    def test_authentication(self):
         user = authenticate(username='testuser', password='secret')
         self.assertTrue((user is not None) and user.is_authenticated)