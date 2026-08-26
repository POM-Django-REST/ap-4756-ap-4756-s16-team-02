from django.urls import path
from order import api as order_api

app_name = "user"

urlpatterns = [
    path("<int:user_id>/order/", order_api.UserOrdersView.as_view(), name="user_orders"),
]
