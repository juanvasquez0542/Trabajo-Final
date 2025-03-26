# importacion de la biblioteca.
from optparse import Option

# diccionario vacio de agenda para almacenar los contactos.
agenda = {} #clave nombre, valor = numero

# definimos la funcion para mostrar los contactos de la agenda.
def mostrar_contactos():
    print("\nNombre".ljust(20) + "Numero de contacto")
    print("-" * 35)
    for nombre, numero in agenda.items():
        print(f"{nombre.ljust(20)}{numero}")

# iniciamos un bucle infinito para mostrar las opciones del menu.
while True:
# demostracion del menu con las opcines disponibles para el usuario.
    print("\nOPCIONES")
    print("1. Añadir nuevo contacto:")
    print("2. Buscar contacto:")
    print("3. Editar contacto:")
    print("4. Listar contactos:")
    print("5. Eliminar contacto:")
    print("6. Salir:")
    Option = int(input("introduce tu eleccion: "))

# varieble de la primera opcion del menu (añadir el contacto)
    if Option == 1:
        nombre = input("nombre del contacto: ")
        numero = input("numero del contacto: ")
        agenda[nombre] = numero
        print("El contacto ha sido añadido")

#variable de la segunda opcion del menu (buscar el contacto)
    elif Option == 2:
        nombre_buscar = input("Nombre del contacto a buscar:")
        if nombre_buscar in agenda:
            print(f"su numero es {agenda[nombre_buscar]}")
        else: 
            print("Contacto no encontrado")

 # variable de la tercera opcion del menu (editar el contacto)
    elif Option == 3:
        nombre_editar = input("Nombre del contacto a editar: ")
        if nombre_editar in agenda:
            nuevo_numero = input("Nuevo número de contacto: ")
            agenda[nombre_editar] = nuevo_numero
            print("Contacto actualizado")
        else:
            print("Contacto no encontrado")

 # variable de la cuarta opcion del menu (listar los contactos)
    elif Option == 4:
        mostrar_contactos()
    
    # variable de la quinta opcion del menu (contactos eliminados)
    elif Option == 5:
        nombre_eliminar = input("Nombre del contacto a eliminar: ")
        if nombre_eliminar in agenda:
            del agenda[nombre_eliminar]
            print("Contacto eliminado")
        else:
            print("Contacto no encontrado")
    # variable de la sexta opcion del menu (salir del progrma)
    elif Option == 6:
        print("¡Hasta luego!")
        break

    # opcion erronea en caso de que no se escoja una del menu (esta no es valida y muestra un error)
    else:
        print("Opción no válida")