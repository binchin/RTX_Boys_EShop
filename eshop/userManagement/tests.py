from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from .views import confirmLogin, user_signUp, user_login
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

class UserTest(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password'

    # def test_signup_page_url(self):
    #     response = self.client.get("signup/")
    #     self.assertNotEqual(response.status_code, 200)

    def test_user_count(self):
        users = get_user_model().objects.all()
        self.assertNotEqual(users.count(), 3)

    def test_authentication(self):
     user = authenticate(username='john', password='secret')
     self.assertFalse((user is not None) and user.is_authenticated)