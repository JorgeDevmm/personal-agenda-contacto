import json


class AgendaDigital:
    # agenda_digital principal de contactos
    _agenda_digital = {}

    # @classmethod
    # def inicializar_agenda(cls):
    #    cls._agenda_digital = {}

    @staticmethod
    def agregar_contacto_agenda(diccionario_contacto, nombre_contacto):
        if nombre_contacto in AgendaDigital._agenda_digital:
            print(f"{nombre_contacto} ya existe, no pudo agregar")
        else:
            # agregar un nuevo contacto al diccionario agenda_digital
            AgendaDigital._agenda_digital[str(nombre_contacto)] = diccionario_contacto
            print('''Se Ingreso un nuevo contacto''')

    @staticmethod
    # método que escribe un fichero
    def escribir_fichero():
        try:
            # Intenta abrir el archivo para lectura y carga el contenido actual
            with open("agenda_fichero.txt", "r") as agenda_fichero:
                contenido = agenda_fichero.read()
                # Intenta cargar el contenido como un diccionario
                agenda_digital_actual = json.loads(contenido) if contenido.strip() else {}
        except FileNotFoundError:
            # Si el archivo no existe crea un diccionario vacio
            agenda_digital_actual = {}

        # Agrega o actualiza el nuevo diccionario
        agenda_digital_actual.update(AgendaDigital._agenda_digital)

        # Escribe el diccionario actualizado en el archivo
        with open("agenda_fichero.txt", "w") as agenda_fichero:

            # Escribir el diccionario en el fichero
            json.dump(agenda_digital_actual, agenda_fichero)
            print("se agrego el contacto en el fichero")

    @staticmethod
    def leer_fichero():

        try:
            with open("agenda_fichero.txt", "r") as agenda_fichero:
                # leer fichero completo para poder validar
                contenido = agenda_fichero.read()
                # verificar si el contenido del archivo es vacío después de eliminar cualquier espacio en blanco
                if contenido.strip():
                    # cerrar el archivo después de leer el contenido, para evitar errores con loads
                    agenda_fichero.close()
                    # cargar el contenido como un diccionario
                    agenda_digital_lectura = json.loads(contenido)
                    return agenda_digital_lectura
                else:
                    return "Archivo vació"
        except Exception as e:
            return "Error", e

    @staticmethod
    # Eliminar el contacto por su nombre clave
    def eliminar_contacto_fichero(nombre_contacto):
        try:
            # Validar si el contacto a eliminar se encuentra en el diccionario
            if nombre_contacto in AgendaDigital._agenda_digital:
                # eliminar contacto del diccionario agenda_digital
                del AgendaDigital._agenda_digital[str(nombre_contacto)]
                print(f"Se elimino el contacto {nombre_contacto}")
                return True
        except KeyError as error:
            print(f"No existe la clave contacto {error}")
            return False
