from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:sign-up')
LOGIN_URL = reverse('user:log-in')
DELETE_USER_URL = reverse('user:delete')


def create_user(**kwargs):
    return  get_user_model().objects.create_user(**kwargs)


class UserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        payload = {
            'email': 'test@gmail.com',
            'password1': 'passWord@1',
            'password2': 'passWord@1'
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(payload['password1']))
        self.assertNotIn('password', response.data)

    def test_create_user_unsuccess(self):
        payload = {
            'email': 'test@gmail.com',
            'password1': 'password1',
            'password2': 'password2'
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
