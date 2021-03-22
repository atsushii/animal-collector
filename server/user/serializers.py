from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core.models import Animal, UserAnimal
from animal.serializers import AnimalSerializer
import time


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
    animals = serializers.SlugRelatedField(many=True, read_only=True,
                                          slug_field='animal_name')

    def create(self, validated_data):
        print(validated_data)
        animal_name = {'animal_name': validated_data.get('animals')[0].animal_name}
        animal = AnimalSerializer(data=animal_name)
        animal.is_valid(raise_exception=True)
        obj = animal.save()
        print('obj', obj)
        validated_data['animals'] = obj
        return UserAnimal.objects.create(**validated_data)

    class Meta:
        model = UserAnimal
        fields = (
            'id', 'picture_url', 'x_coordinate',
            'y_coordinate', 'created_date',
            'animals'
        )
        read_only_fields = ('id',)

