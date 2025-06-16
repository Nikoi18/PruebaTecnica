# Proyecto de Gestión de Inventario Full-Stack

Una aplicación web para la gestión de inventario, construida con un backend en Django Rest Framework que sirve a un frontend moderno y reactivo en Vue.js.
![image](https://github.com/user-attachments/assets/58de089e-3571-419b-aaba-7c3f46e7bdbd)
![image](https://github.com/user-attachments/assets/c91805cb-c94f-44c4-a644-fb07448128e5)
![image](https://github.com/user-attachments/assets/c128d096-e7b8-49ea-adb2-a4c172a45aa5)
![image](https://github.com/user-attachments/assets/659a0a7c-ee1a-4608-b850-3e9cae460e2f)





## 📜 Descripción del Proyecto

Este proyecto es una solución integral para el seguimiento del stock de productos en un almacén. Permite a los usuarios autenticados ver el inventario actual,
añadir nuevos productos, actualizar las cantidades de stock y consultar un historial detallado de todos los movimientos (entradas y salidas). La aplicación 
cuenta con una interfaz limpia, responsiva y un selector de tema claro/oscuro para una mejor experiencia de usuario.

## ✨ Características Principales

-   **Autenticación de Usuarios:** Sistema de login seguro con tokens JWT (Access y Refresh tokens).
-   **Gestión de Inventario (CRUD):**
    -   **Crear:** Añadir nuevos ítems al inventario con SKU, EAN13 y cantidad inicial.
    -   **Leer:** Listar todo el stock disponible en una tabla clara y ordenada.
    -   **Actualizar:** Modificar la cantidad de stock de cualquier ítem.
-   **Historial de Movimientos:** Registro automático de cada entrada o salida de stock, mostrando qué cambió, cuánto y cuándo.
-   **Interfaz Moderna:** Frontend construido con Vue 3 (Composition API) y estilizado para ser limpio y fácil de usar.
-   **Tema Claro/Oscuro:** Selector de tema que guarda la preferencia del usuario en su navegador.

## 🛠️ Tecnologías Utilizadas

### Backend
-   **Python 3**
-   **Django 4+**
-   **Django Rest Framework** para la creación de la API REST.
-   **Simple JWT** para la autenticación con JSON Web Tokens.
-   **PostgreSQL** como base de datos.
-   **django-cors-headers** para gestionar los permisos de Cross-Origin.

### Frontend
-   **Vue.js 3** (con Composition API y `<script setup>`).
-   **Vue Router** para la gestión de rutas (Login, Inventario).
-   **Axios** para las peticiones a la API del backend.
-   **CSS Moderno** con Variables para un theming dinámico (claro/oscuro).

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para instalar y correr el proyecto en un entorno de desarrollo local.

### Prerrequisitos

Asegúrate de tener instalado el siguiente software:
-   [Python 3.8+](https://www.python.org/downloads/)
-   [Node.js 16+](https://nodejs.org/) y npm
-   [PostgreSQL](https://www.postgresql.org/download/)
-   [Git](https://git-scm.com/downloads/)

## Clonar el Repositorio
```bash
git clone https://github.com/Nikoi18/PruebaTecnica

BACKEND
Navega hasta la carpeta o directorio
cd backend

# Crear el entorno
python -m venv venv
# Activar en Windows
# venv\Scripts\activate
# Activar en macOS/Linux
source venv/bin/activate
Tambien puedes usar pipenv, pipenv install

Luego instalas las dependencias
pip install -r requirements.txt
Luego has las migraciones y crea el superusuario (seran las mismas credenciales para iniciar session)
python manage.py migrate
python manage.py createsuperuser

Ahora configuremos el Frontend
Navega hasta la carpeta frontend
instala las dependencias de node.js
npm install

por ultimo Ejecutar la aplicacion, necesitaras las dos terminales abiertas simultaneamente
usa python manage.py runserver por el lado del backend y npm run serve por el lado del frontend 


