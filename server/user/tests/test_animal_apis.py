from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Animal


LOGIN_URL = reverse('user:log-in')
REGISTER_ANIMAL = reverse('user:register-animal')
ANIMAL_REGISTER_URL = reverse('animal:animal-register')


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


def register_animal(**kwargs):
    return Animal.objects.create(**kwargs)


class UserAnimalTests(TestCase):

    def setUp(self):
        payload = {
            'email': 'test@gmail.com',
            'password': 'password'
        }

        create_user(**payload)
        self.client = APIClient()
        response = self.client.post(LOGIN_URL, payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

        self.animal_obj = register_animal(animal_name='cat')

    def test_register_animal_by_authorized_user(self):
        payload = {
            'picture_url': 'http://test.com',
            'x_coordinate': 1.2,
            'y_coordinate': 1.2,
            'animal': {'animal_name': 'cat'}
        }
        response = self.client.post(REGISTER_ANIMAL, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
