from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import InventoryItem, StockMovement
from .serializers import InventoryItemSerializer, StockMovementSerializer


class InventoryList(generics.ListCreateAPIView):

    queryset = InventoryItem.objects.all().order_by('sku')
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        with transaction.atomic():
            item_instance = serializer.save()
            if item_instance.quantity > 0:
                StockMovement.objects.create(
                    item=item_instance,
                    quantity_change=item_instance.quantity,
                    reason="Creación inicial de stock"
                )


class InventoryItemDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):

        original_quantity = serializer.instance.quantity

        with transaction.atomic():

            item_instance = serializer.save()          

            quantity_change = item_instance.quantity - original_quantity


            if quantity_change != 0:
                StockMovement.objects.create(
                    item=item_instance,
                    quantity_change=quantity_change,
                    reason="Actualización desde la App"
                )


class StockMovementHistory(generics.ListAPIView):

    queryset = StockMovement.objects.all().order_by('-timestamp')
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]