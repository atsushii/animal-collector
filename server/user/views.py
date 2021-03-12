from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import UserSerializer, UserLoginSerializer, UserAnimalSerializer
from core.models import UserAnimal


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class UserAnimalRegister(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer

class UserManager(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class =UserSerializer

    def get_object(self):
        return self.request.user

class UserAnimalRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer

