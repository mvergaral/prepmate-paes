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

### Estilos con Ionic y Tailwind

El proyecto utiliza **Ionic** junto a **Tailwind CSS**. Para aplicar utilidades
de Tailwind sobre componentes `ion-*` se crearon clases globales definidas en
`src/global.scss`. Por ejemplo `ion-item-custom`, `ion-input-custom` e
`ion-button-custom` permiten replicar los estilos definidos en Figma y mantener
compatibilidad con el modo oscuro. Estas reglas aprovechan el selector
`::part(native)` de Ionic para que los estilos se apliquen correctamente sobre
el elemento interno del componente. Revisa dicho archivo para añadir nuevas
utilidades y aplícalas como clases en tus vistas. Las vistas de autenticación
(login y registro) usan estas utilidades dentro de un contenedor `w-96` para
igualar la maqueta de referencia.

### Modo claro/oscuro

El `ThemeService` gestiona la clase `dark` en el elemento `<html>` para
habilitar el tema oscuro. `src/global.scss` importa
`@ionic/angular/css/palettes/dark.class.css` de forma que los componentes de
Ionic respondan a esta misma clase y mantengan coherencia con Tailwind.
Puedes alternar el tema llamando a `themeService.toggleTheme()` como se muestra
en `home.page.ts`.

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
flask db migrate -m "Mensaje de migración"
flask db upgrade
```

### 6. Ejecutar el servidor Flask

```bash
flask run
```

El backend estará corriendo en: [http://localhost:5000](http://localhost:5000)

### 7. Ejecutar los tests y ver cobertura

```bash
pytest --cov=app backend/tests/
```

### 8. Poblar la base de datos con datos de prueba

Para generar información de ejemplo puedes ejecutar el script `seed.py` desde la
carpeta `backend`:

```bash
python seed.py
```

Este comando crea usuarios, materias y ejercicios básicos para iniciar el
desarrollo.

---

## Redis en el Proyecto

El backend utiliza **Redis** como sistema de almacenamiento en memoria para funcionalidades que requieren alta velocidad y persistencia temporal.


### Instalación y uso de Redis

1. **Instala Redis en tu sistema:**
   - Ubuntu/Debian:
     ```bash
     sudo apt-get update
     sudo apt-get install redis-server
     ```
   - Mac (Homebrew):
     ```bash
     brew install redis
     ```

2. **Inicia el servicio Redis:**
   ```bash
   redis-server
   ```
   O en sistemas con systemd:
   ```bash
   sudo service redis-server start
   ```

3. **Verifica que Redis está corriendo:**
   ```bash
   redis-cli ping
   ```
   Debería responder con: `PONG`

4. **Variables de entorno para Redis:**
   Puedes personalizar la conexión a Redis agregando estas variables a tu archivo `.env`:
   ```env
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_DB=0
   ```
   Si no las defines, se usarán los valores por defecto mostrados arriba.

5. **Dependencia Python:**
   La librería `redis` ya está incluida en `requirements.txt`.

> Si necesitas cambiar la configuración de conexión (host/puerto), edita la línea correspondiente en `app/services/auth_middleware.py`.

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

## 📘 API Reference

Para ver la documentación completa de la API, consulta [API_DOCS.md](backend/API_DOCS.md).

## Postman

Importar este archivo en Postman para ejecutar las peticiones de ejemplo a la API.
[postman/PrepMatePAES.postman_collection.json](postman/PrepMatePAES.postman_collection.json)

El archivo contiene ejemplos de peticiones a los endpoints de la API, incluyendo autenticación, gestión de usuarios, materias y ejercicios.
Además, incluye scripts para automatizar la autenticación y el manejo de tokens.
En caso de ser necesario, puedes modificar las variables de entorno en Postman para adaptarlas a la configuración local.
