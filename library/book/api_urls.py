from django.urls import path

from . import api

app_name = "book"

urlpatterns = [
    path("<int:id>/", api.book_detail, name="book_detail"),
]
