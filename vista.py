import controlador
# Módulos externos
import os
from rich.console  import Console
from rich.progress import track
from time import sleep 

console = Console(width=100)

def clear():
    try:
        return os.system('clear')
    except:
        return os.system('cls')

def barra_progreso():
    for step in track(range(100), description="[blue]Procesando"):
            sleep(0.01)
    clear()

def vista_abm():
    # Bandera:
    incorrecto_abm = 0
    valuerror_abm = 0
    
    while True:
        clear()

        console.rule("", style="bold gold3")
        console.print("DISQUERÍA FORMOSA MUSICAL", justify="center", style="bold white on deep_sky_blue4")
        console.rule("", style="bold gold3")
        console.print("MENÚ ABM\n", style="bold deep_sky_blue3", justify="center")
        console.print("1 - [bold]ALTA DE ÁLBUM[/]")
        console.print("2 - [bold]BAJA DE ÁLBUM[/]")
        console.print("3 - [bold]MODIFICACIÓN DE ÁLBUM[/]")
        console.print("4 - [bold italic red]SALIR[/]\n")
        
        try:
            if incorrecto_abm == 1:
                console.print("[i]¡Opción [bold red]incorrecta[/]![/i] :flushed:")
            if valuerror_abm == 1:
                console.print("[i]Ingrese solo [bold gold3]números[/], por favor[/i] :confused:.")
            opcion = int(console.input("[i]Ingrese su [bold cyan]opción[/][/i] :smiley:: ")) 
            assert opcion <= 6
        except ValueError:
            valuerror_abm = 1
            incorrecto_abm = 0 
            continue
        except AssertionError:
            incorrecto_abm = 1
            valuerror_abm = 0
            continue
        
        if opcion == 1:
            barra_progreso()
            controlador.InsertarAlbum()
        elif opcion == 2:
            barra_progreso()
            controlador.ListarAlbumesPorArtistas()
        elif opcion == 3:
            controlador.ListarAlbumesPorGenero()
        elif opcion == 4:
            print("")
            break
        # Resetear bandera para el regreso:
        incorrecto_abm = 0
        valuerror_abm = 0
        
# Es un "parche". Necesita mejora.
valuerror = 0    
incorrecto = 0

while True:
    clear()

    from rich import box
    from rich.table import Table
    from rich.align import Align

    console.rule("", style="bold gold3")
    console.print("DISQUERÍA FORMOSA MUSICAL", justify="center", style="bold white on deep_sky_blue4")
    console.rule("", style="bold gold3")

    tabla_principal = Table(box=box.ROUNDED, show_header=False, style="bold gold3")
    tabla_principal.add_row("[bold gold3]MENÚ PRINCIPAL")
    console.print(Align.center(tabla_principal))

    tabla_opcion = Table(expand=True, style="deep_sky_blue3", box=box.DOUBLE_EDGE, show_header=False, highlight=True)
    tabla_opcion.add_row("[cyan bold]1[/] - [bold]ALTA, BAJA O MODIFICACIÓN DE UN ÁLBUM[/]")
    tabla_opcion.add_row("[cyan bold]2[/] - [bold]LISTADO DE ÁLBUMES POR ARTISTAS[/]")
    tabla_opcion.add_row("[cyan bold]3[/] - [bold]LISTADO DE ÁLBUMES POR GÉNERO MUSICAL[/]")
    tabla_opcion.add_row("[cyan bold]4[/] - [bold]BÚSQUEDA POR NOMBRE DE ÁLBUM[/]")
    tabla_opcion.add_row("[cyan bold]5[/] - [bold]INSERTAR INTERPRETE[/]") # EXTRA
    tabla_opcion.add_row("[cyan bold]6[/] - [bold italic red1]SALIR[/]") 
    console.print(tabla_opcion)

    try:
        if incorrecto == 1:
            tabla_incorrecto = Table(expand=True, style="red1", box=box.ASCII, show_header=False, highlight=True)
            tabla_incorrecto.add_row("[i]¡Opción [bold red1]incorrecta[/]![/i] :flushed:")
            console.print(tabla_incorrecto)

        if valuerror == 1:
            tabla_error = Table(expand=True, style="dark_orange3", box=box.ASCII, show_header=False, highlight=True)
            tabla_error.add_row("[i]Ingrese solo [bold dark_orange3]números[/], por favor[/i] :confused:.")
            console.print(tabla_error)
        
        tabla_op = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False, highlight=True)
        tabla_op.add_row("[i]Ingrese su [bold cyan]opción[/][/i] :smiley:: ")
        console.print(tabla_op)
        opcion = int(console.input("[bold cyan]>: "))

        assert opcion <= 6
    except ValueError:
        valuerror = 1
        incorrecto = 0 
        continue
    except AssertionError:
        incorrecto = 1
        valuerror = 0
        continue
    
    if opcion == 1:
        vista_abm()
    elif opcion == 2:
        barra_progreso()
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 3:
        barra_progreso()
        controlador.ListarAlbumesPorGenero()
    elif opcion == 4:
        None
    elif opcion == 5:
        None
    elif opcion == 6:
        console.print("\n[italic bold]¡[gold1]Gracias[/], nos vemos![/] :sunglasses:\n")
        break

    # Resetear bandera para el regreso:
    incorrecto = 0
    valuerror = 0