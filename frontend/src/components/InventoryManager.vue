<template>
  <div class="inventory-layout">
    <div class="card add-item-card">
      <h3>Añadir Nuevo Ítem</h3>
      <form @submit.prevent="handleAddItem" class="add-item-form">
        <input type="text" v-model="newItem.sku" placeholder="SKU" class="form-input" required />
        <input type="text" v-model="newItem.ean13" placeholder="EAN13" class="form-input" required />
        <input type="number" v-model.number="newItem.quantity" placeholder="Cantidad" class="form-input" required />
        <button type="submit" class="btn-primary">Añadir</button>
      </form>
    </div>

    <div class="card">
      <h3>📈 Listado de Stock</h3>
      <table class="styled-table">
        <thead>
          <tr>
            <th>SKU</th>
            <th>EAN13</th>
            <th>Stock Actual</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in inventory" :key="item.id">
            <td data-label="SKU">{{ item.sku }}</td>
            <td data-label="EAN13">{{ item.ean13 }}</td>
            <td data-label="Stock">
              <input type="number" v-model.number="item.quantity" @change="markAsChanged(item)" class="table-input" />
            </td>
            <td data-label="Acción" class="action-buttons">
              <button @click="updateStock(item)" :disabled="!item.changed" class="btn-secondary">
                Actualizar
              </button>
              <button @click="handleDeleteItem(item)" class="btn-delete">
                Borrar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <h3>📜 Historial de Movimientos</h3>
      <table class="styled-table">
        <thead>
          <tr>
            <th>SKU</th>
            <th>Cambio</th>
            <th>Fecha y Hora</th>
            <th>Motivo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="movement in movements" :key="movement.id">
            <td data-label="SKU">{{ movement.item_sku }}</td>
            <td data-label="Cambio" :class="movement.quantity_change > 0 ? 'entrada' : 'salida'">
              {{ movement.quantity_change > 0 ? '+' : '' }}{{ movement.quantity_change }}
            </td>
            <td data-label="Fecha">{{ new Date(movement.timestamp).toLocaleString() }}</td>
            <td data-label="Motivo">{{ movement.reason }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';
import apiClient from '../api.js'; 

const inventory = ref([]);
const movements = ref([]);
const newItem = reactive({
  sku: '',
  ean13: '',
  quantity: 0,
});

const fetchInventory = async () => {
  try {
    const response = await apiClient.get('/inventory/');
    inventory.value = response.data.map(item => ({ ...item, changed: false }));
  } catch (error) {
    console.error("Error fetching inventory:", error);
    alert("Error al cargar el inventario.");
  }
};

const fetchMovements = async () => {
  try {
    const response = await apiClient.get('/movements/');
    movements.value = response.data;
  } catch (error) {
    console.error("Error fetching movements:", error);
    alert("Error al cargar el historial de movimientos.");
  }
};

const markAsChanged = (item) => {
  item.changed = true;
};

const updateStock = async (item) => {
  try {
    await apiClient.patch(`/inventory/${item.id}/`, {
      quantity: item.quantity
    });
    item.changed = false;
    alert(`Stock de ${item.sku} actualizado correctamente.`);
    await fetchInventory();
    await fetchMovements();
  } catch (error) {
    console.error(`Error updating ${item.sku}:`, error);
    alert(`Error al actualizar el stock de ${item.sku}.`);
  }
};

const handleAddItem = async () => {
  try {
    await apiClient.post('/inventory/', newItem);
    alert(`Ítem ${newItem.sku} añadido correctamente.`);
    newItem.sku = '';
    newItem.ean13 = '';
    newItem.quantity = 0;
    await fetchInventory();
    await fetchMovements();
  } catch (error) {
    console.error("Error adding item:", error);
    alert("Error al añadir el ítem. Verifique que los datos sean únicos y correctos.");
  }
};

const handleDeleteItem = async (itemToDelete) => {
  if (window.confirm(`¿Estás seguro de que quieres borrar el ítem ${itemToDelete.sku}? Esta acción no se puede deshacer.`)) {
    try {
      await apiClient.delete(`/inventory/${itemToDelete.id}/`);
      alert(`Ítem ${itemToDelete.sku} ha sido eliminado.`);
      await fetchInventory();
      await fetchMovements(); 
    } catch (error) {
      console.error(`Error deleting ${itemToDelete.sku}:`, error);
      alert('Hubo un error al eliminar el ítem.');
    }
  }
};

onMounted(() => {
  fetchInventory();
  fetchMovements();
});
</script>

<style scoped src="./styles/InventoryManager.css"></style>