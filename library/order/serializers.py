from authentication.models import CustomUser
from book.models import Book
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(
        source="book",
        queryset=Book.objects.all(),
        many=False,
    )
    user_id = serializers.PrimaryKeyRelatedField(
        source="user",
        queryset=CustomUser.objects.all(),
        many=False,
    )

    class Meta:
        model = Order

        fields = ["id", "book_id", "user_id", "created_at", "planned_end_at", "end_at"]
