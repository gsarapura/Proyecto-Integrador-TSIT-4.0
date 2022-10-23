import controlador



def ABMAlbum():
    while True:
        print("\n+-------------------------------------------+")
        print("|         DISQUERÍA FORMOSA MUSICAL         |")
        print("+-------------------------------------------+\n")
        print("")
        print("MENÚ DE ALTA / BAJA / MODIFICACIÓN DE ÁLBUMES\n")
        print("1 - NUEVO ÁLBUM")
        print("2 - MODIFICAR ÁLBUM")
        print("3 - ELIMINAR ÁLBUM")
        print("4 - VOLVER AL MENÚ PRINCIPAL")
        print("\n")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            controlador.InsertarAlbum()
        elif opcion == 2:
            controlador.ModificarAlbum()
        elif opcion == 3:
            controlador.EliminarAlbum()
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
    print("1 - ALTA / BAJA / MODIFICACION DE UN ÁLBUM")
    print("2 - LISTADO DE ÁLBUMES POR ARTISTAS")
    print("3 - LISTADO DE ÁLBUMES POR GÉNERO MUSICAL")
    print("4 - BÚSQUEDA POR NOMBRE DE ÁLBUM")
    print("5 - INSERTAR INTERPRETE") # EXTRA
    print("6 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        ABMAlbum()
    elif opcion == 2:
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 3:
        controlador.ListarAlbumesPorGenero()
    elif opcion == 4:
        None
    elif opcion == 5:
        None
    elif opcion == 6:
        break
    else:
        print("¡Opción incorrecta!")
