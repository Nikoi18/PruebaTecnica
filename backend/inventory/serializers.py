from rest_framework import serializers
from .models import InventoryItem, StockMovement

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'sku', 'ean13', 'quantity']

class StockMovementSerializer(serializers.ModelSerializer):
    item_sku = serializers.CharField(source='item.sku', read_only=True)

    class Meta:
        model = StockMovement
        fields = ['id', 'item_sku', 'quantity_change', 'timestamp', 'reason']