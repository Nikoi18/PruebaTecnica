from django.db import models

class InventoryItem(models.Model):
    sku = models.CharField(max_length=100, unique=True, verbose_name='SKU')
    ean13 = models.CharField(max_length=13, unique=True, verbose_name='EAN13')
    quantity = models.IntegerField(verbose_name='Cantidad de Stock')

    def __str__(self):
        return f"{self.sku}({self.quantity})"
    
class StockMovement(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, verbose_name='Item o movimientos')
    quantity_change = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, default="Actualizacion manual")

    def __str__(self):
        return f"{self.item.sku} - Cambio {self.quantity_change} el {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
