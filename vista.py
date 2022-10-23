import controlador

def vista_abm():
    while True:
        print("\n+-------------------------------------------+")
        print("|         DISQUERÍA FORMOSA MUSICAL         |")
        print("+-------------------------------------------+\n")
        print("")
        print("MENÚ ABM\n")
        print("1 - ALTA DE ÁLBUM")
        print("2 - BAJA DE ÁLBUM")
        print("3 - MODIFICACIÓN DE ÁLBUM")
        print("4 - SALIR")
        print("\n")
        try:
            opcion = int(input("Ingrese su opción: "))
        except ValueError:
            print("Ingrese solo números, por favor.")
            continue 

        if opcion == 1:
            controlador.InsertarAlbum()
        elif opcion == 2:
            controlador.ListarAlbumesPorArtistas()
        elif opcion == 3:
            controlador.ListarAlbumesPorGenero()
        elif opcion == 4:
            break
        else:
            print("¡Opción incorrecta!")
        
while True:
    print("\n+-------------------------------------------+")
    print("|         DISQUERÍA FORMOSA MUSICAL         |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("1 - ALTA, BAJA O MODIFICACIÓN DE UN ÁLBUM")
    print("2 - LISTADO DE ÁLBUMES POR ARTISTAS")
    print("3 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL")
    print("4 - BÚSQUEDA POR NOMBRE DE ÁLBUM")
    print("5 - INSERTAR INTERPRETE") # EXTRA
    print("6 - SALIR\n")
    try:
        opcion = int(input("Ingrese su opción: "))
    except ValueError:
        print("Ingrese solo números, por favor.")
        continue 

    if opcion == 1:
        vista_abm()
    elif opcion == 2:
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 3:
        controlador.ListarAlbumesPorGenero()
    elif opcion == 4:
        None
    elif opcion == 5:
        None
    elif opcion == "":
        print("Solo ingrese números.")
    elif opcion == 6:
        break
    else:
        print("¡Opción incorrecta!")