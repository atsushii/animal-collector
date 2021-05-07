from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core.models import UserAnimal
from animal.serializers import AnimalSerializer
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
root.addHandler(handler)


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
        return token


class AnimalField(serializers.StringRelatedField):
    def to_internal_value(self, data):
        return data


class UserAnimalSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(many=False, read_only=False)

    def create(self, validated_data):

        animal_name = validated_data.pop('animal')
        serializer = AnimalSerializer(data=dict(animal_name))
        serializer.is_valid(raise_exception=True)

        obj = serializer.save()
        validated_data['animal'] = obj

        return UserAnimal.objects.create(**validated_data)

    class Meta:
        model = UserAnimal
        fields = (
            'id', 'file', 'x_coordinate',
            'y_coordinate', 'created_date',
            'animal'
        )
        depth = 1
        read_only_fields = ('id',)
