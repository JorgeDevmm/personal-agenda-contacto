import menu as m


def creacion_agenda():
    """Proceso de creación de la agenda.

    Inicializa el menú y ejecuta un bucle para manejar las opciones de usuario.

    Opciones del menú:
        1. Lee la agenda digital del fichero.
        2. Solicita los datos de un nuevo contacto por pantalla.
        3. Crea un nuevo contacto en la agenda digital.
        4. Escribe la agenda resultante en un fichero.
        5. Eliminar un contacto del fichero.
        6. Salir.

    :return: None
    """
    continuar = True

    while continuar:
        opcion = m.inicializar_menu()

        # se ejecuta si solo la opción es diferente a 7
        if opcion != 7:
            m.elegir_opciones(opcion)
            continuar = input("Desea continuar con otra operación s/n?: ")
            if continuar == 's' or continuar == "si" or continuar == "SI" or continuar == "S":
                continuar = True
            else:
                continuar = False
                print("Programa finalizado")
        elif opcion == 7:
            continuar = False
            print("Programa finalizado")


if __name__ == '__main__':
    creacion_agenda()
