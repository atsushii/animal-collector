from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core.models import Animal, UserAnimal


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Password must be match')
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']

        return self.Meta.model.objects.create_user(**data)

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'password1', 'password2'
        )
        read_only_fields = ('id',)


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        print(user_data)
        return token


class UserAnimalSerializer(serializers.ModelSerializer):
    animals = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Animal.objects.all()
    )


    class Meta:
        model = UserAnimal
        fields = (
            'id', 'picture_url', 'x_coordinate',
            'y_coordinate', 'created_date',
            'animals'
        )
        read_only_fields = ('id',)
