from rest_framework import serializers

from core.models import Animal, UserAnimal, User


class AnimalSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        try:
            obj = Animal.objects.get(animal_name=validated_data['animal_name'])
        except Animal.DoesNotExist:
            new_value = {'animal_name': validated_data['animal_name'],
                         'description': validated_data['description']}
            obj = Animal(**new_value)
            obj.save()
        return obj

    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ('id',)