from rest_framework import serializers
from django.db import IntegrityError

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Author
<<<<<<< HEAD
        fields = ["id", "name", "surname", "patronymic"]
=======
        fields = ['id', 'name', 'surname', 'patronymic']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError as e:
            raise serializers.ValidationError(
                {"detail": str(e)}
            )

    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except IntegrityError as e:
            raise serializers.ValidationError(
                {"detail": str(e)}
            )
>>>>>>> 08fbaa73d8c73587670c2f6255cd72ad7523e9a9
