from rest_framework import serializers

from core.models import Animal, UserAnimal, User


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ('id',)


class UserAnimalSerializer(serializers.ModelSerializer):
    animals = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Animal.objects.all()
    )

    users = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = UserAnimal
        fields = (
            'id', 'picture_url', 'x_coordinate',
            'y_coordinate', 'created_date',
            'animals', 'users'
        )
        read_only_fields = ('id',)