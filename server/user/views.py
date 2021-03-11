from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, UserLoginSerializer, UserAnimalSerializer
from core.models import UserAnimal


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class UserAnimalRegister(generics.CreateAPIView):
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer


class UserAnimalRetrieveView(generics.RetrieveAPIView):
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer
