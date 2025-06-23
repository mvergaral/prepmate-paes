# Documentación Técnica

Este documento describe la arquitectura y los componentes principales del sistema **PrepMate PAES**.

## Arquitectura general

- **Frontend**: construido con [Angular](https://angular.io/) e [Ionic](https://ionicframework.com/) para la construcción de aplicaciones web híbridas. Se usa [Tailwind CSS](https://tailwindcss.com/) para la personalización de estilos.
- **Backend**: implementado con [Flask](https://flask.palletsprojects.com/) y [SQLAlchemy](https://www.sqlalchemy.org/) como ORM. La autenticación se realiza mediante _JSON Web Tokens_ (JWT) y se exponen rutas REST para todas las operaciones.
- **Base de Datos**: PostgreSQL es el motor utilizado. Las migraciones se gestionan con `Flask-Migrate` (Alembic).
- **Redis**: se emplea como almacenamiento en memoria para funcionalidades que requieren velocidad, como colas de notificaciones.

## Estructura de carpetas

```
backend/
  app/
    controllers/       # Blueprints de Flask
    models/            # Definición de modelos SQLAlchemy
    repositories/      # Capas de acceso a datos
    services/          # Lógica de negocio y utilidades
    schemas/           # Serialización con Marshmallow
    routes.py          # Registro de blueprints
  migrations/          # Archivos de Alembic
  tests/               # Pruebas unitarias y de integración
frontend/
  prepmate/
    src/               # Código fuente de la aplicación Angular/Ionic
    tailwind.config.js # Configuración de Tailwind CSS
postman/
  *.postman_collection.json # Colección de ejemplos para Postman
```

## Configuración básica

1. **Variables de entorno**: se leen desde un archivo `.env` en la carpeta `backend`. Deben definirse la URL de la base de datos (`DATABASE_URL`) y la clave de JWT (`JWT_SECRET_KEY`).
2. **Entorno virtual**: en `backend/venv` se encuentra un entorno Python para las dependencias. Para activarlo:
   ```bash
   source backend/venv/bin/activate
   ```
3. **Instalación de dependencias**: utiliza el archivo `backend/requirements.txt`.
   ```bash
   pip install -r backend/requirements.txt
   ```

## Scripts de utilidad

- `backend/run.py`: punto de entrada de la aplicación Flask.
- `backend/seed.py`: script para poblar la base de datos con datos de ejemplo.
- `frontend/prepmate/package.json`: contiene los comandos de npm para desarrollo del frontend, como `ionic serve` y `ng build`.

## Pruebas automatizadas

Las pruebas de backend se encuentran en `backend/tests`. Para ejecutarlas junto a la generación de reporte de cobertura:
```bash
pytest --cov=app backend/tests/
```

## Despliegue

El proyecto está pensado para ejecutarse de forma local durante el desarrollo. Para un despliegue en producción se recomienda:

- Configurar un servidor WSGI como Gunicorn o uWSGI para el backend.
- Servir el frontend como archivos estáticos (por ejemplo con Nginx).
- Asegurar las variables sensibles mediante un administrador de secretos o variables de entorno en el servidor.

