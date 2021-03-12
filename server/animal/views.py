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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnimalDetail(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(
            user=self.request.user
        )
