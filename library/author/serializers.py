from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Author
        fields = ["id", "name", "surname", "patronymic"]
