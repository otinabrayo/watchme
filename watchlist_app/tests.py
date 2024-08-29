from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION= 'Token '+ self.token.key)
        
        # Manual create a platform so we can test the list and individual platform   
        self.stream = models.StreamPlatform.objects.create(name='Netflix',
                                                           about='Stream number 1',
                                                           website='https://netflix.com')
                
    def test_streamplatform_create(self):
        data = {
            'name': ' Netflix',
            'about': 'Stream number 1',
            "website" : "https//netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, 403)
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, 200)
        
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, 200)
        
    def test_streamplatform_put(self):
        response = self.client.put(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, 403)
        
    def test_streamplatform_delete(self):
        response = self.client.delete(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, 403)
        

class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION= 'Token '+ self.token.key)
        
        # Manual create a platform so we can test the list and individual platform   
        self.stream = models.StreamPlatform.objects.create(name='Netflix',
                                                           about='Stream number 1',
                                                           website='https://netflix.com') 
        self.watchlist = models.WatchList.objects.create(platform=self.stream, 
                                                         title='Stream',
                                                         storyline= 'Stream')   
                
    def test_watchlist_create(self):
        data = {
            'title': 'The Shawshank Redemption',
            'storyline': 'A banker is wrongfully convicted and sent to prison for 20 years',
            'platform': self.stream,
            'active' : True,
        }
        response = self.client.post(reverse('movie_list'), data)
        self.assertEqual(response.status_code, 403)
    
    def test_watchlist_list(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_watchlist_ind(self):
        response = self.client.get(reverse('movie_details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title,'Stream')