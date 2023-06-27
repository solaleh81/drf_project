from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestcase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                             about="#1 Streaming Platform", 
                                             website="https://netflix.com")
    def test_streamplatform_create(self):
        data = {
            "name": "Netflix", 
            "about": "#1 Streaming Platform", 
            "website": "https://netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.post(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_ind(self):
        response = self.client.post(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WatchListTestcase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                             about="#1 Streaming Platform", 
                                             website="https://netflix.com")



                                             
        self.watchlist = models.WatchList.objects.create(platform=self.stream, 
            title="Example Movie",
            storyline="Example Story",
            active=True)

    def test_whacthlist_create(self):
        data = {
            "platform": self.stream, 
            "title": "Example Movie",
            "storyline": "Example Story",
            "active": True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_whacthlist_list(self):
        response = self.client.post(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_whacthlist_ind(self):
        response = self.client.post(reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')


class ReviewTestcase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                             about="#1 Streaming Platform", 
                                             website="https://netflix.com")
        
                                             
        self.watchlist = models.WatchList.objects.create(platform=self.stream, 
            title="Example Movie",
            storyline="Example Story",
            active=True)
                                                         
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, 
            title="Example Movie",
            storyline="Example Story",
            active=True)
        self.review = models.Review.objects.create(review_user=self.user, rating=5,
            description="Great Movie!",
            watchlist=self.watchlist2,
            active=True)


# booooooooooog

    def test_review_create(self):
        data = {
            "review_user": self.user, 
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(models.Review.objects.count(), 1)
        self.assertEqual(models.Review.objects.get().rating, 5)

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



    def test_review_create_unauth(self):
        data = {
            "review_user": self.user, 
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }

        self.client.force_authenticate(user=None)

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_review_review_update(self):
        data = {
            "review_user": self.user, 
            "rating": 4,
            "description": "Great Movie! - Updated",
            "watchlist": self.watchlist,
            "active": False
        }
        response = self.client.put(reverse('review-detail', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_review_user(self):
        response = self.client.get('/watch/review/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



    
