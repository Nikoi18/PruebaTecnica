from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import InventoryItem, StockMovement
from .serializers import InventoryItemSerializer, StockMovementSerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]


class InventoryItemUpdate(generics.UpdateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_quantity = request.data.get('quantity')

        if new_quantity is not None:
            quantity_change = int(new_quantity) - instance.quantity

            StockMovement.objects.create(
                item=instance,
                quantity_change=quantity_change,
                reason=f"Actualización desde la App"            )

            instance.quantity = new_quantity
            instance.save()
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class StockMovementHistory(generics.ListAPIView):
    queryset = StockMovement.objects.all().order_by('-timestamp')
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]