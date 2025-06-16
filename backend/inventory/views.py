from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import InventoryItem, StockMovement
from .serializers import InventoryItemSerializer, StockMovementSerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]


class InventoryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_quantity = request.data.get('quantity')

        if new_quantity is not None:

            try:
                quantity_change = int(new_quantity) - instance.quantity
                if quantity_change != 0:
                    StockMovement.objects.create(
                        item=instance,
                        quantity_change=quantity_change,
                        reason=f"Actualización desde la App"
                    )
            except (ValueError, TypeError):

                pass
        

        return super().update(request, *args, **kwargs)

class StockMovementHistory(generics.ListAPIView):
    queryset = StockMovement.objects.all().order_by('-timestamp')
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]