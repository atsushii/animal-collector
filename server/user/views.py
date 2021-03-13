from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import UserSerializer, LoginSerializer, UserAnimalSerializer
from core.models import UserAnimal


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


class UserAnimalRetrieveView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(
            user=self.request.user
        )


