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

## Requisitos

- **Python**: 3.x
- **Django**: 3.x o superior
- **Django REST Framework**: 3.x o superior

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```

4. Inicia el servidor:
    ```bash
    python manage.py runserver
    ```

5. Accede a la API en `http://127.0.0.1:8000/`.

## Autenticación

La API utiliza autenticación por token. Para obtener un token, envía una solicitud `POST` a `/api-token-auth/` con el nombre de usuario y contraseña del usuario registrado.

Ejemplo de solicitud `POST` para obtener un token:

```bash
curl -X POST -d "username=tu_usuario&password=tu_contraseña" http://127.0.0.1:8000/api-token-auth/

