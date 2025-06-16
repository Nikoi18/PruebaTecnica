<template>
  <div class="inventory-container">
    <h2>📈 Listado de Stock de Inventario</h2>
    <table>
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
          <td>{{ item.sku }}</td>
          <td>{{ item.ean13 }}</td>
          <td>
            <input type="number" v-model.number="item.quantity" @change="markAsChanged(item)" />
          </td>
          <td>
            <button @click="updateStock(item)" :disabled="!item.changed">
              Actualizar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <hr />

    <h2>📜 Historial de Movimientos</h2>
    <table>
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
          <td>{{ movement.item_sku }}</td>
          <td :class="movement.quantity_change > 0 ? 'entrada' : 'salida'">
             {{ movement.quantity_change > 0 ? '+' : '' }}{{ movement.quantity_change }}
          </td>
          <td>{{ new Date(movement.timestamp).toLocaleString() }}</td>
          <td>{{ movement.reason }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// --- CONFIGURACIÓN ---
// Pega aquí el token de acceso que obtuviste del backend.
// En una app real, esto vendría de un proceso de login.
const accessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUwMDk5NTQxLCJpYXQiOjE3NTAwOTkyNDEsImp0aSI6ImE1NTJhOTU3ZjZiYTQ5NDg4ODIwYzZjY2YzMmUyMGI3IiwidXNlcl9pZCI6MX0.NU1r6juDBZTER4Kmxq-D5bbAkL3dEVQ302SP44XPa4I'; 

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: {
    Authorization: `Bearer ${accessToken}`
  }
});

// --- ESTADO REACTIVO ---
const inventory = ref([]);
const movements = ref([]);

// --- MÉTODOS ---
const fetchInventory = async () => {
  try {
    const response = await apiClient.get('/inventory/');
    inventory.value = response.data.map(item => ({ ...item, changed: false }));
  } catch (error) {
    console.error("Error al obtener el inventario:", error);
    alert("Error al cargar el inventario. ¿Está el token JWT configurado y es válido?");
  }
};

const fetchMovements = async () => {
  try {
    const response = await apiClient.get('/movements/');
    movements.value = response.data;
  } catch (error) {
    console.error("Error al obtener los movimientos:", error);
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
    // Refrescar el historial para ver el nuevo movimiento
    await fetchMovements();
  } catch (error) {
    console.error(`Error al actualizar ${item.sku}:`, error);
    alert(`Error al actualizar el stock.`);
  }
};

// --- LIFECYCLE HOOK ---
onMounted(() => {
  fetchInventory();
  fetchMovements();
});
</script>

<style scoped>
.inventory-container {
  max-width: 900px;
  margin: auto;
  font-family: sans-serif;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #f2f2f2;
}
input[type="number"] {
  width: 70px;
  padding: 5px;
}
button {
  padding: 5px 10px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
}
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
hr {
  margin: 40px 0;
}
.entrada {
    color: green;
    font-weight: bold;
}
.salida {
    color: red;
    font-weight: bold;
}
</style>