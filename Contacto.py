class Contacto:

    # constructor
    def __init__(self, nombre, direccion, email, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono

    # 1. estableces un diccionario con los nombres del contacto
    def crear_contacto(self, nombre_contacto):
        """ Creo un diccionario e ingreso los valores del diccionario por consola

        :param nombre_contacto: (str) nombre a utilizar como clave de diccionario y nombre del mismo
        :return nombre_contacto con los datos almacenados
        """
        nombre_contacto = {"nombre": self.nombre, "direccion": self.direccion,
                           "email": self.email, "telefono": self.telefono}

        print(nombre_contacto)
        return nombre_contacto
