from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        required=False, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "password",
            "created_at",
            "updated_at",
            "role",
            "is_active",
        ]
