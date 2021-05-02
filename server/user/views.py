from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, mixins
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, LoginSerializer, UserAnimalSerializer
from core.models import UserAnimal


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class DeleteUserView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def delete(self, request, *args, **kwargs):

        user_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            print(f'delete: {user_id}')
        return response

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        return obj


class UserAnimalRegister(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAnimal.objects.all()
    serializer_class = UserAnimalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserManager(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

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
