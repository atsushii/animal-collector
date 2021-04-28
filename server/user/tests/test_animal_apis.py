from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


LOGIN_URL = reverse('user:log-in')
REGISTER_ANIMAL = reverse('user:register-animal')
LIST_ANIMAL_URL = reverse('user:list-animals')


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class UserAnimalTests(TestCase):

    def setUp(self):
        user_payload = {
            'email': 'test@gmail.com',
            'password': 'password'
        }

        self.animal_payload = {
            'picture_url': 'http://test.com',
            'x_coordinate': 1.2,
            'y_coordinate': 1.2,
            'animal': {'animal_name': 'cat'}
        }

        create_user(**user_payload)
        self.client = APIClient()
        self.unauthorized_client = APIClient()
        response = self.client.post(LOGIN_URL, user_payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    def test_register_animal_by_authorized_user(self):
        response = self.client.post(REGISTER_ANIMAL, self.animal_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_animal_by_unauthorized_user(self):
        response = self.unauthorized_client.post(REGISTER_ANIMAL, self.animal_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_animal_by_authorized_user(self):
        response = self.client.post(REGISTER_ANIMAL, self.animal_payload, format='json')
        RETRIEVE_ANIMAL_URL = reverse('user:retrieve-animal', args=[response.data['id']])

        animal = self.client.get(RETRIEVE_ANIMAL_URL)

        self.assertEqual(animal.status_code, status.HTTP_200_OK)
        self.assertEqual(animal.data['id'], response.data['id'])
        self.assertEqual(animal.data['picture_url'], self.animal_payload['picture_url'])
        self.assertEqual(animal.data['x_coordinate'], self.animal_payload['x_coordinate'])
        self.assertEqual(animal.data['y_coordinate'], self.animal_payload['y_coordinate'])
        self.assertEqual(animal.data['animal']['animal_name'], self.animal_payload['animal']['animal_name'])

    def test_list_stored_animals_by_authorized_user(self):
        self.client.post(REGISTER_ANIMAL, self.animal_payload, format='json')
        self.animal_payload['animal']['animal_name'] = 'dog'
        self.client.post(REGISTER_ANIMAL, self.animal_payload, format='json')

        animals = self.client.get(LIST_ANIMAL_URL)

        self.assertEqual(animals.status_code, status.HTTP_200_OK)
        self.assertEqual(len(animals.data), 2)
        self.assertTrue(i['animal']['animal_name'] in ['cat', 'dog'] for i in animals.data)