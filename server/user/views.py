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

    def _params_to_ints(self, qs):
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        animals = self.request.query_params.get('animals')
        queryset = self.queryset

        if animals:
            animal_ids = self._params_to_ints('animals')
            queryset = queryset.filter(animals__id__in=animal_ids)


        return queryset.filter(
            user=self.request.user
        )


