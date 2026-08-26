from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderListView(APIView):
    def check_version(self, version: str) -> bool:
        return version == "v1"

    def get_permissions(self):
        return [permissions.IsAdminUser()]

    def get(self, request: Request, version: str) -> Response:
        if self.check_version(version):
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({"error": "Invalid version"}, status=HTTP_400_BAD_REQUEST)

    def post(self, request: Request, version: str) -> Response:
        if self.check_version(version):
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({"error": "Invalid version"}, status=HTTP_400_BAD_REQUEST)


class OrderDetailsView(APIView):
    def check_version(self, version: str) -> bool:
        return version == "v1"

    def get_permissions(self):
        return [permissions.IsAdminUser()]

    def get(self, request: Request, id: int, version: str) -> Response:
        if self.check_version(version):
            order = get_object_or_404(Order, id=id)
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({"error": "Invalid version"}, status=HTTP_400_BAD_REQUEST)

    def put(self, request: Request, id: int, version: str) -> Response:
        if self.check_version(version):
            order = get_object_or_404(Order, id=id)
            serializer = OrderSerializer(instance=order, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response({"error": "Invalid version"}, status=HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int, version: str) -> Response:
        if self.check_version(version):
            order = get_object_or_404(Order, id=id)
            order.delete()
            return Response(status=HTTP_204_NO_CONTENT)

        return Response({"error": "Invalid version"}, status=HTTP_400_BAD_REQUEST)
