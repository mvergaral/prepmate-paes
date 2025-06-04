# prepmate-paes

Aplicación de apoyo para preparación de la PAES.

## Integrante

- Matías Vergara

## Frontend

Para ejecutar el frontend primero debemos entrar al directorio del frontend y luego instalar las dependencias:

```bash
cd frontend/prepmate
npm install
```

Luego, para ejecutar el frontend, ejecutamos el siguiente comando:

```bash
ionic serve
```

---

## Backend

Para ejecutar el backend, sigue los siguientes pasos desde el directorio raíz del proyecto:

### 1. Entrar a la carpeta del backend

```bash
cd backend
```

### 2. Activar el entorno virtual

```bash
source venv/bin/activate
```

### 3. Configurar las variables de entorno

Edita el archivo `.env` con tus credenciales de PostgreSQL:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/prepmate
FLASK_ENV=development
FLASK_APP=run.py
```

### 4. Crear la base de datos (si aún no existe)

```bash
createdb prepmate
```

### 5. Aplicar las migraciones a la base de datos

```bash
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Ejecutar el servidor Flask

```bash
flask run
```

El backend estará corriendo en: [http://localhost:5000](http://localhost:5000)

---

### Extras

- Para instalar nuevas dependencias y registrar sus versiones:

  ```bash
  pip install <paquete>
  pip freeze > requirements.txt
  ```

- Para salir del entorno virtual:

  ```bash
  deactivate
  ```
