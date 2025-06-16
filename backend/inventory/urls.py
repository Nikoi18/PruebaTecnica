from django.urls import path
from .views import InventoryList, InventoryItemDetail, StockMovementHistory

urlpatterns = [
    path('inventory/', InventoryList.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryItemDetail.as_view(), name='inventory-detail'),
    path('movements/', StockMovementHistory.as_view(), name='movement-history'),
]