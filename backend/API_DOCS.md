# PrepMate PAES API Documentation

Esta guía describe los endpoints disponibles en el backend de PrepMate PAES.

## Introducción

La API está construida con **Flask** y utiliza **JSON Web Tokens (JWT)** para la autenticación de usuarios.
Todas las respuestas se devuelven en formato JSON.

## Autenticación

1. **Registro de estudiante**
   - **POST /auth/signup**
   - Crea un usuario con rol `student` y devuelve un `access_token`.
2. **Registro de administrador**
   - **POST /auth/signup-admin**
   - Similar al registro de estudiante pero crea un usuario con rol `admin`.
3. **Inicio de sesión**
   - **POST /auth/login**
   - Requiere `email` y `password` en el cuerpo de la solicitud y devuelve un `access_token` válido.
4. **Cerrar sesión**
   - **POST /auth/logout**
   - Requiere encabezado `Authorization: Bearer <token>` y revoca el token.

El token JWT devuelto debe incluirse en el encabezado `Authorization` para acceder a las rutas protegidas.

## Rutas protegidas

- **GET /protected/me** – Devuelve información básica del usuario autenticado.
- **POST /profile** – Crea el perfil de un estudiante.
- **PUT /profile** – Actualiza datos del perfil del estudiante.
- **GET /profile** – Obtiene el perfil del estudiante autenticado.

Todas requieren el encabezado `Authorization` con el token JWT.

## Materias (Subjects)

| Método | Ruta                     | Descripción               |
|-------|-------------------------|---------------------------|
| POST  | `/subjects`             | Crear una nueva materia   |
| GET   | `/subjects`             | Listar todas las materias |
| GET   | `/subjects/<id>`        | Obtener una materia       |
| PUT   | `/subjects/<id>`        | Actualizar una materia    |
| DELETE| `/subjects/<id>`        | Eliminar una materia      |

Ejemplo de creación:

```bash
curl -X POST http://localhost:5000/subjects \
     -H 'Content-Type: application/json' \
     -d '{"name": "Matemática M1", "description": "desc", "area": "Matemáticas"}'
```

## Ejercicios (Exercises)

| Método | Ruta                       | Descripción                |
|-------|---------------------------|----------------------------|
| POST  | `/exercises`              | Crear un ejercicio         |
| GET   | `/exercises`              | Listar todos los ejercicios|
| GET   | `/exercises/<id>`         | Obtener un ejercicio       |
| PUT   | `/exercises/<id>`         | Actualizar un ejercicio    |
| DELETE| `/exercises/<id>`         | Eliminar un ejercicio      |

El campo `options` debe ser un objeto JSON con las alternativas (por ejemplo `{"A": "1", "B": "2"}`).

## Manejo de errores

La API devuelve códigos HTTP estándar. Cuando ocurre un error, la respuesta incluye un campo `message` con la descripción del problema.

Ejemplo:

```json
{"message": "Token de autenticación requerido"}
```

## Ejemplos de uso con cURL

```bash
# Login
token=$(curl -s -X POST http://localhost:5000/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"user@test.com","password":"1234"}' | jq -r '.access_token')

# Acceder a /protected/me
curl -H "Authorization: Bearer $token" http://localhost:5000/protected/me
```

