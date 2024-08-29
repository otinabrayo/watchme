from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            'username': 'testcase',
            'email': 'testcase@example.com',
            'password': 'testcase',
            'password1': 'testcase'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 201)
        
    
class LoginLogoutTestCase(APITestCase):
    
    def setUp(self):
        # Create the use
        self.user = User.objects.create_user(username='example', password='pass@123')
        # Create the token for the user    
        self.token = Token.objects.create(user=self.user)
        
    # def test_1_login(self):
    #     data = {
    #         'username': 'example',
    #         'password': 'pass@123'
    #     }
    #     response = self.client.post(reverse('login'), data)
    #     self.assertEqual(response.status_code, 200)
        
    # def test_2_logout(self):
    #     self.token = Token.objects.get(user__username='example')
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    #     response = self.client.post(reverse('logout'))
    #     self.assertEqual(response.status_code, 200)
