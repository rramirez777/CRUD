import json
import os

class Usuario:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def to_dict(self):
        return {"Nombre": self.nombre, "Edad": self.edad}


class BaseDeDatos:
    def __init__(self, archivo="database.json"):
        self.archivo = archivo
        self.database = self.cargar_db()

    def cargar_db(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return {}

    def guardar_db(self):
        with open(self.archivo, "w") as f:
            json.dump(self.database, f)

    def agregar_usuario(self, usuario):
        self.database[usuario.id] = usuario.to_dict()
        self.guardar_db()
        print(f"Usuario {usuario.nombre} agregado correctamente.\n")

    def mostrar_usuarios(self):
        print("\nUsuarios registrados:")
        if not self.database:
            print("No hay usuarios registrados.\n")
        else:
            for id, info in self.database.items():
                print(f"ID: {id} | Nombre: {info['nombre']} | Edad: {info['edad']}")
            print()

    def actualizar_usuario(self, id, nuevo_nombre, nueva_edad):
        if id in self.database:
            self.database[id] = {"nombre": nuevo_nombre, "edad": nueva_edad}
            self.guardar_db()
            print("Usuario actualizado correctamente.\n")
        else:
            print("Usuario no encontrado.\n")

    def eliminar_usuario(self, id):
        if id in self.database:
            del self.database[id]
            self.guardar_db()
            print("Usuario eliminado correctamente.\n")
        else:
            print("Usuario no encontrado.\n")

db = BaseDeDatos()

while True:
    print("=== MENÚ DE GESTIÓN ===")
    print("1. Crear usuario")
    print("2. Ver usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        id = input("ID del usuario: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        nuevo_usuario = Usuario(id, nombre, edad)
        db.agregar_usuario(nuevo_usuario)

    elif opcion == "2":
        db.mostrar_usuarios()

    elif opcion == "3":
        id = input("ID del usuario a actualizar: ")
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_edad = input("Nueva edad: ")
        db.actualizar_usuario(id, nuevo_nombre, nueva_edad)

    elif opcion == "4":
        id = input("ID del usuario a eliminar: ")
        db.eliminar_usuario(id)

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.\n")
