import controlador
import os
from rich.progress import track
from time import sleep


def clear(): 
    try:
        return os.system('clear')
    except:
        return os.system('cls')

while True:
    clear()
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
     
    clear()

    if opcion == 1:
        controlador.InsertarAlbum()
    elif opcion == 2:
        for step in track(range(100), description="[blue]Procesando..."):
            sleep(0.01)
        clear()
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 3:
        for step in track(range(100), description="[blue]Procesando..."):
            sleep(0.01)
        clear()
        controlador.ListarAlbumesPorGenero()
    elif opcion == 4:
        None
    elif opcion == 5:
        None
    elif opcion == 6:
        break
    else:
        print("¡Opción incorrecta!")