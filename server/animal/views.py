from rest_framework import generics, viewsets, mixins
from rest_framework import permissions

from core.models import Animal, UserAnimal, User

from animal.serializers import \
    AnimalSerializer, \
    AnimalDetailSerializer


class AnimalRegisterView(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(
            user=self.request.user
        )
