from rest_framework import serializers

from core.models import Animal, UserAnimal, User
from animal.wikipedia.api import AnimalDataProcessing


class AnimalSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        animal_data_processing = AnimalDataProcessing(validated_data['animal_name'])
        description = animal_data_processing.scraper()

        try:
            obj = Animal.objects.get(animal_name=validated_data['animal_name'])
        except Animal.DoesNotExist:
            new_value = {'animal_name': validated_data['animal_name'],
                         'description': description}
            obj = Animal(**new_value)
            obj.save()
        return obj

    class Meta:
        model = Animal
        fields = ['animal_name',]
        read_only_fields = ('id',)