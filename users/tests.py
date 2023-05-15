from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy

from users.models import MaralUser


class UserTest(APITestCase):
    fixtures = ["users/fixtures/001_user.json"]

    def setUp(self):
        self.url = reverse('user_list')
        admin = mommy.make(MaralUser)
        self.client.force_authenticate(admin)

    def test_list_of_all_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

