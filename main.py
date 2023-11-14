import menu as m


def creacion_agenda():
    continuar = True

    while continuar:
        opcion = m.inicializar_menu()

        # se ejecuta si solo la opción es diferente a 6
        if opcion != 6:
            m.elegir_opciones(opcion)
            continuar = input("Desea continuar con otra operación s/n?: ")
            if continuar == 's' or continuar == "si" or continuar == "SI" or continuar == "S":
                continuar = True
            else:
                continuar = False
                print("Programa finalizado")
        elif opcion == 6:
            continuar = False
            print("Programa finalizado")


if __name__ == '__main__':
    creacion_agenda()
