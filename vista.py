import controlador
# Módulos externos
import os
from rich.console  import Console
from rich.progress import track
from time import sleep 

console = Console(width=80)

def clear():
    try:
        return os.system('clear')
    except:
        return os.system('cls')

def vista_abm():
    while True:
        console.rule("", style="bold gold3")
        console.print("DISQUERÍA FORMOSA MUSICAL", justify="center", style="bold white on deep_sky_blue4")
        console.rule("", style="bold gold3")
        console.print("MENÚ ABM\n", style="bold deep_sky_blue3", justify="center")
        console.print("1 - [bold]ALTA DE ÁLBUM[/]")
        console.print("2 - [bold]BAJA DE ÁLBUM[/]")
        console.print("3 - [bold]MODIFICACIÓN DE ÁLBUM[/]")
        console.print("4 - [bold italic red]SALIR[/]\n")
        
        try:
            opcion = int(console.input("[i]Ingrese su [bold cyan]opción[/][/i] :smiley:: ")) 
        except ValueError:
            console.print("[i]Ingrese solo [bold gold3]números[/], por favor[/i] :confused:.")
            continue 
        if opcion == 1:
            controlador.InsertarAlbum()
        elif opcion == 2:
            controlador.ListarAlbumesPorArtistas()
        elif opcion == 3:
            controlador.ListarAlbumesPorGenero()
        elif opcion == 4:
            print("")
            break
        else:
            print("¡Opción incorrecta!")
# MMMM es un parche. Necesita mejora.
valuerror = 2    
incorrecto = 2

while True:
    clear()

    console.rule("", style="bold gold3")
    console.print("DISQUERÍA FORMOSA MUSICAL", justify="center", style="bold white on deep_sky_blue4")
    console.rule("", style="bold gold3")
    console.print("MENÚ PRINCIPAL\n", style="bold dark_orange3", justify="center")
    console.print("1 - [bold]ALTA, BAJA O MODIFICACIÓN DE UN ÁLBUM[/]")
    console.print("2 - [bold]LISTADO DE ÁLBUMES POR ARTISTAS[/]")
    console.print("3 - [bold]LISTADO DE ÁLBUMES POR GÉNERO MUSICAL[/]")
    console.print("4 - [bold]BÚSQUEDA POR NOMBRE DE ÁLBUM[/]")
    console.print("5 - [bold]INSERTAR INTERPRETE[/]") # EXTRA
    console.print("6 - [bold italic red]SALIR[/]\n")

    

    try:
        if valuerror == 1:
            console.print("[i]Ingrese solo [bold gold3]números[/], por favor[/i] :confused:.")
            incorrecto = 0
        if incorrecto == 1:
            console.print("[i]¡Opción [bold red]incorrecta[/]![/i] :flushed:")
            #valuerror = 0
        opcion = int(console.input("[i]Ingrese su [bold cyan]opción[/][/i] :smiley:: ")) 
    except ValueError:
        valuerror = 1
        continue 
    
    valuerror = 0
    incorrecto = 0

    if opcion == 1:
        vista_abm()
    elif opcion == 2:
        for step in track(range(100), description="[blue]Procesando"):
            sleep(0.01)
        clear()
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 3:
        for step in track(range(100), description="[blue]Procesando"):
            sleep(0.01)
        clear()
        controlador.ListarAlbumesPorGenero()
    elif opcion == 4:
        None
    elif opcion == 5:
        None
    elif opcion == 6:
        console.print("\n[italic bold]¡[gold1]Gracias[/], nos vemos![/] :sunglasses:\n")
        break
    else:
        incorrecto = 1