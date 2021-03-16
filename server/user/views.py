from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .serializers import UserSerializer, LoginSerializer, UserAnimalSerializer
from animal.serializers import AnimalSerializer
from core.models import UserAnimal, Animal


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserAnimalRegister(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserManager(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class =UserSerializer

    def get_object(self):
        return self.request.user


class UserAnimalListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class UserAnimalRetrieve(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
