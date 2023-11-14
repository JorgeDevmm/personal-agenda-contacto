import json


class AgendaDigital:
    # agenda_digital principal de contactos
    _agenda_digital = {}

    @classmethod
    def inicializar_agenda(cls):
        cls._agenda_digital = {}

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
        # abre si no existe y sobreescribe si existe y cierra un fichero correctamente, w escritura, r lectura default
        with open("agenda_fichero.txt", "w") as agenda_fichero:
            # Inicializar el diccionario antes de cargar los datos del archivo
            AgendaDigital.inicializar_agenda()

            # Escribir el diccionario en el fichero
            json.dump(AgendaDigital._agenda_digital, agenda_fichero)
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
