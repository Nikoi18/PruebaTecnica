from django.urls import path
from .views import InventoryList, InventoryItemUpdate, StockMovementHistory

urlpatterns = [
    path('inventory/', InventoryList.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryItemUpdate.as_view(), name='inventory-update'),
    path('movements/', StockMovementHistory.as_view(), name='movement-history'),
]