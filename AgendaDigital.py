import json


class AgendaDigital:
    # agenda_digital principal de contactos
    _agenda_digital = {}

    @staticmethod
    def agregar_contacto_agenda(diccionario_contacto, nombre_contacto):
        """
        Escribir la agenda creada en un diccionario
        :param diccionario_contacto: dict que representa a un contacto
        :param nombre_contacto: str que representa al contacto
        :return:
        """
        if nombre_contacto in AgendaDigital._agenda_digital:
            print(f"{nombre_contacto} ya existe, no pudo agregar")
        else:
            # agregar un nuevo contacto al diccionario agenda_digital
            AgendaDigital._agenda_digital[str(nombre_contacto)] = diccionario_contacto
            print('''Se Ingreso un nuevo contacto''')

    @staticmethod
    # método que escribe un fichero
    def escribir_fichero(clave_eliminar=None):
        """
        Escribe el diccionario de la agenda digital en un archivo.

        :param clave_a_eliminar: Clave opcional a eliminar del diccionario actualizado
        :return: None
        """
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

        # Elimina la clave especificada si se proporciona, solo si escogió la opción elimminar
        if clave_eliminar is not None and clave_eliminar in agenda_digital_actual:
            # Eliminar del fichero
            del agenda_digital_actual[clave_eliminar]

        # Escribe el diccionario actualizado en el archivo
        with open("agenda_fichero.txt", "w") as agenda_fichero:

            # Escribir el diccionario en el fichero
            json.dump(agenda_digital_actual, agenda_fichero)
            print("se agrego el contacto en el fichero")

    @staticmethod
    def leer_fichero():
        """
        Lee el contenido del archivo de la agenda digital.

        :return: Diccionario que representa la agenda digital.
        """
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
        """
        Elimina un contacto del archivo de la agenda digital.

        :param nombre_contacto: Nombre del contacto a eliminar.
        :return: True si se eliminó correctamente, False si no se encontró el contacto.
        """
        try:
            # obtengo el fiche en una variable tipo diccionario
            AgendaDigital._agenda_digital = AgendaDigital.leer_fichero()
            # Validar si el contacto a eliminar se encuentra en el diccionario
            if nombre_contacto in AgendaDigital._agenda_digital:
                # eliminar contacto del diccionario agenda_digital
                del AgendaDigital._agenda_digital[nombre_contacto]
                print(f"Se elimino el contacto {nombre_contacto}")
                return True
        except KeyError as error:
            print(f"No existe la clave contacto {error}")
            return False

    def buscar_contacto_fichero(nombre_contacto):
        """
        Busca un contacto en el archivo de la agenda digital.

        :param nombre_contacto: Nombre del contacto a buscar.
        :return: Diccionario que representa al contacto si se encuentra, None si no se encuentra.
        """
        # obtengo el fiche en una variable tipo diccionario
        AgendaDigital._agenda_digital = AgendaDigital.leer_fichero()
        try:
            # válido si existe el contacto como clave en el diccionario del fichero
            if nombre_contacto in AgendaDigital._agenda_digital:
                # devuelve el diccionario con la clave de contacto
                return AgendaDigital._agenda_digital[nombre_contacto]
        except Exception as e:
            print("Error en la búsqueda", e)
