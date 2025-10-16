# Sistema de gestión simple (con JSON)

Este proyecto es un ejemplo básico de cómo realizar operaciones de base de datos (crear, leer, actualizar y eliminar) utilizando Python y un archivo JSON como almacenamiento local.

## Funcionalidades
- Registrar nuevos usuarios mediante consola.
- Guardar la información en un archivo `data.json`.
- Consultar, actualizar o eliminar datos registrados.

## Requisitos
- Python 3.x (no se requieren librerías externas)

## Estructura del proyecto


### Ejemplo de contenido del archivo database.json:

    {
        "001": {
            "nombre": "Ana",
            "edad": "21"
        },
        "002": {
            "nombre": "Luis",
            "edad": "30"
        }
    }


### Ejemplo de Funcionamiento:
  
    === MENÚ DE GESTIÓN ===
    1. Crear usuario
    2. Ver usuarios
    3. Actualizar usuario
    4. Eliminar usuario
    5. Salir
    Elige una opción: 1
     ID del usuario: 001
     Nombre: Ana
     Edad: 21
     Usuario Ana agregado correctamente.
