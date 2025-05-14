# Restaurant API

Esta es una API para gestionar menús y reservas en un restaurante. Además, cuenta con autenticación de usuarios mediante tokens.

## Rutas disponibles

### 1. Autenticación y Usuarios

- **`/api/users/`**:  
  - GET: Obtener la lista de usuarios registrados.
  - POST: Crear un nuevo usuario.

- **`/api-token-auth/`**:  
  - POST: Obtener un token de autenticación para un usuario registrado. Requiere un payload JSON con las credenciales:
    ```json
    {
      "username": "usuario",
      "password": "contraseña"
    }
    ```

### 2. Menú y Reservas

- **`/menu/`**:  
  - GET: Obtener una lista de los menús disponibles.
  - POST: Crear un nuevo menú.

- **`/menu/<id>/`**:  
  - GET: Obtener un menú específico.
  - PUT: Actualizar un menú existente.
  - DELETE: Eliminar un menú.

- **`/reserva/`**:  
  - GET: Obtener la lista de reservas.
  - POST: Crear una nueva reserva.

- **`/reserva/<id>/`**:  
  - GET: Obtener una reserva específica.
  - PUT: Actualizar una reserva existente.
  - DELETE: Eliminar una reserva.

### 3. Página principal

- **`/home`**:  
  - GET: Ver la página principal del sitio.

### 4. Autenticación de la API

- **`/api-auth/`**:  
  - URL de autenticación predeterminada proporcionada por Django REST Framework para acceder a la interfaz de autenticación básica y autenticación de sesión.

### 5. Panel de administración

- **`/admin/`**:  
  - Acceso al panel de administración de Django.

