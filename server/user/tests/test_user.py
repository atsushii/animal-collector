from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:sign-up')
LOGIN_URL = reverse('user:log-in')
DELETE_USER_URL = reverse('user:delete')
RETRIEVE_USER = reverse('user:me')


def create_user(**kwargs):
    return  get_user_model().objects.create_user(**kwargs)


class PublicUserApiTests(TestCase):

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

    def test_create_user_invalid_password(self):
        payload = {
            'email': 'test@gmail.com',
            'password1': 'password1',
            'password2': 'password2'
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_exist(self):
        payload1 = {
            'email': 'test@gmail.com',
            'password': 'passWord@1',
        }

        payload2 = {
            'email': 'test@gmail.com',
            'password1': 'passWord@1',
            'password2': 'passWord@1'
        }

        create_user(**payload1)

        response = self.client.post(CREATE_USER_URL, payload2)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_login_user(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'passWord@1',
        }

        create_user(**payload)

        response = self.client.post(LOGIN_URL, payload)
        self.assertIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_token_for_invalid_credentials(self):
        payload1 = {
            'email': 'test@gmail.com',
            'password': 'passWord@1',
        }

        payload2 = {
            'email': 'test@gmail.com',
            'password': 'wrong',
        }
        create_user(**payload1)
        response = self.client.post(LOGIN_URL, payload2)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)

    def test_create_token_missing_field(self):
        payload = {
            'email': 'test@gmail.com',
            'password': '',
        }
        response = self.client.post(LOGIN_URL, payload)

        self.assertNotIn('access', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_by_unauthorized_user(self):
        response = self.client.get(RETRIEVE_USER)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):

    def setUp(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'Password1',
        }

        self.user = create_user(**payload)
        self.client = APIClient()

        response = self.client.post(LOGIN_URL,
                                    payload)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    def test_retrieve_profile(self):
        response = self.client.get(RETRIEVE_USER)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_delete_user(self):
        response = self.client.delete(DELETE_USER_URL)
        user = get_user_model().objects.all()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(user), 0)
