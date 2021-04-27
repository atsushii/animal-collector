from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class UserAnimalTests(TestCase):

    def setUp(self):
        self.client = APIClient()


