from AgendaDigital import AgendaDigital
from Contacto import Contacto

diccionario_contacto = None
nombre_contacto = ""


def inicializar_menu():
    print('''AGENDA CONTACTOS
1. Lee la agenda digital del fichero
2. Solicita los datos de un nuevo contacto por pantalla al usuario
3. Crea un nuevo contacto en la agenda digital
4. Escribe la agenda resultante en un fichero
5. Eliminar contacto a buscar del fichero
6. Buscar contacto en el fichero
7. Salir
        ''')
    # insertar opción a ejecutar
    try:

        opcion = int(input("Ingresar la opción: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            return "Opción no valida"
    except Exception as e:
        return "Elegir una opción valida", e


def elegir_opciones(opcion):
    # global para reutilizar las variable en todo el documento
    global diccionario_contacto, nombre_contacto
    # validar opciones
    if 1 <= opcion and opcion < 7:
        if opcion == 1:
            mostrar_fichero = AgendaDigital.leer_fichero()
            print(mostrar_fichero)
        elif opcion == 2:
            diccionario_contacto, nombre_contacto = obtener_contacto_para_agregar()
        elif opcion == 3:
            if diccionario_contacto and nombre_contacto:
                # agrego el diccionario contacto y nombre de contacto como índice al diccionario principal
                AgendaDigital.agregar_contacto_agenda(diccionario_contacto, nombre_contacto)
            else:
                print("Primero debes crear un contacto en la opción 2")
        elif opcion == 4:
            AgendaDigital.escribir_fichero()
        elif opcion == 5:
            nombre_contacto_eliminar = input("Ingresar el nombre de contacto a eliminar: ")
            if AgendaDigital.eliminar_contacto_fichero(nombre_contacto_eliminar.upper()):
                AgendaDigital.escribir_fichero(nombre_contacto_eliminar)
            else:
                print("Contacto a eliminar no válido o no existe")
        elif opcion == 6:
            nombre_contacto_buscar = input("Ingresar el nombre de contacto a buscar: ")
            if AgendaDigital.buscar_contacto_fichero(nombre_contacto_buscar.upper()) is None:
                print("No se encontró contacto")
            else:
                print(AgendaDigital.buscar_contacto_fichero(nombre_contacto_buscar.upper()))



    else:
        print("Opción no válida")


def solicitar_datos():
    nombre = input("Ingresar nombre: ")
    direccion = input("Ingresar Direccion: ")
    email = input("Ingresar Email: ")
    telefono = input("Ingresar Telefono: ")

    return nombre.upper(), direccion.upper(), email.upper(), telefono.upper()


def obtener_contacto_para_agregar():
    global diccionario_contacto, nombre_contacto
    # Ingreso el nombre de contacto que será la clave por contacto
    nombre_contacto = input("Ingresar el nombre de contacto: ")
    # obtenemos el diccionario contacto con los datos establecidos
    nombre, direccion, email, telefono = solicitar_datos()
    # Creamos un objeto tipo contacto
    instancia_contacto = Contacto(nombre, direccion, email, telefono)
    # creamos el diccionario de contacto y devolvemos un diccionario contacto
    diccionario_contacto = instancia_contacto.crear_contacto(nombre_contacto.upper())

    return diccionario_contacto, nombre_contacto.upper()
