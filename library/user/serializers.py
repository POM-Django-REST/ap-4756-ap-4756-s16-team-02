from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import IntegrityError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email',
                'created_at', 'updated_at', 'role', 'is_active']

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