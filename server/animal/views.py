from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from core.models import Animal, UserAnimal, User

from animal.serializers import \
    AnimalSerializer, \
    UserAnimalSerializer,\
    AnimalDetailSerializer


class AnimalRegisterView(generics.CreateAPIView):

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetail(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer

