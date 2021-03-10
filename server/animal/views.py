from rest_framework import generics

from core.models import Animal, UserAnimal, User

from animal.serializers import \
    AnimalSerializer, \
    UserAnimalSerializer,\
    AnimalDetailSerializer


class AnimalView(generics.CreateAPIView):
    queryset = AnimalSerializer.objects.all()
    serializer_class = AnimalSerializer