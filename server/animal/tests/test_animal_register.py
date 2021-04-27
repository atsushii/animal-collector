from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Animal


ANIMAL_REGISTER_URL = reverse('animal:animal-register')
LOGIN_URL = reverse('user:log-in')


def create_user(*args, **kwargs):
    return get_user_model().objects.create_user(**kwargs)


class RegisterAnimalTests(TestCase):

    def setUp(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'password'
        }
        create_user(**payload)
        self.client = APIClient()
        self.client2 = APIClient()

        response = self.client.post(LOGIN_URL, payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    def test_register_new_animal_by_authorized_user(self):
        payload = {
            'animal_name': 'cat',
        }
        response = self.client.post(ANIMAL_REGISTER_URL, payload)
        animal = Animal.objects.last()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(animal.animal_name, payload['animal_name'])
        self.assertTrue(len(animal.description) > 0)

    def test_register_animal_by_unauthorized_user(self):
        payload = {
            'animal_name': 'cat'
        }
        response = self.client2.post(ANIMAL_REGISTER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

