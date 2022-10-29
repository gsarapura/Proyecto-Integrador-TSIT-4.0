import controlador
import modelo
## Módulos externos
import os
from rich.console  import Console
# Crear tablas:
from rich import box
from rich.table import Table
from rich.align import Align
#Crear barra:
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

def tabla_artistas_vigentes():
    con = modelo.Conectar()
    # Rich
    table = Table(title="Estos son los Intérpretes vigentes actualmente:")
    columnas = ["ID", "APELLIDO", "NOMBRE", "NACIONALIDAD", "URL FOTO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarInterprete():
        table.add_row(str(i[0]), str(i[2]), str(i[1]), str(i[3]), str(i[4]))

    console.print(Align.center(table))

def ABMInterprete():
    # Bandera:
    incorrecto_abm = 0
    valuerror_abm = 0
    
    while True:
        clear()

        console.rule("", style="bold gold3")
        console.print("DISQUERÍA FORMOSA MUSICAL", justify="center", style="bold white on deep_sky_blue4")
        console.rule("", style="bold gold3")

        tabla_principal = Table(box=box.ROUNDED, show_header=False, style="bold purple")
        tabla_principal.add_row("[bold purple]ABM INTÉRPRETE")
        console.print(Align.center(tabla_principal))

        tabla_opcion = Table(expand=True, style="orange_red1", box=box.DOUBLE_EDGE, show_header=False)
        tabla_opcion.add_row("[cyan bold]1[/] - [bold]ALTA DE INTÉRPRETE[/]")
        tabla_opcion.add_row("[cyan bold]2[/] - [bold]BAJA DE INTÉRPRETE[/]")
        tabla_opcion.add_row("[cyan bold]3[/] - [bold]MODIFICACIÓN DE INTÉRPRETE[/]")
        tabla_opcion.add_row("[cyan bold]4[/] - [bold italic red1]SALIR[/]") 
        console.print(tabla_opcion)

        try:
            if incorrecto_abm == 1:
                tabla_incorrecto = Table(expand=True, style="red1", box=box.ASCII, show_header=False)
                tabla_incorrecto.add_row("[i]¡Opción [bold red1]incorrecta[/]![/i] :flushed:")
                console.print(tabla_incorrecto)

            if valuerror_abm == 1:
                tabla_error = Table(expand=True, style="red1", box=box.ASCII, show_header=False)
                tabla_error.add_row("[i]Ingrese solo [bold red1]números[/], por favor[/i] :confused:.")
                console.print(tabla_error)
            
            tabla_op = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False)
            tabla_op.add_row("[i]Ingrese su [bold cyan]opción[/][/i] :smiley:: ")
            console.print(tabla_op)
            opcion = int(console.input("[bold cyan]>: "))
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
            tabla_artistas_vigentes()
            controlador.InsertarInterprete()
        elif opcion == 2:
            barra_progreso()
            tabla_artistas_vigentes()
            controlador.EliminarInterprete()
        elif opcion == 3:
            barra_progreso()
            tabla_artistas_vigentes()
            controlador.ModificarInterprete()
        elif opcion == 4:
            print("")
            break
        # Resetear bandera para el regreso:
        incorrecto_abm = 0
        valuerror_abm = 0

def ABMAlbum():
    # Bandera:
    incorrecto_abm = 0
    valuerror_abm = 0
    
    while True:
        clear()

        console.rule("", style="bold gold3")
        console.print("DISQUERÍA FORMOSA MUSICAL", justify="center", style="bold white on deep_sky_blue4")
        console.rule("", style="bold gold3")

        tabla_principal = Table(box=box.ROUNDED, show_header=False, style="bold chartreuse3")
        tabla_principal.add_row("[bold chartreuse3]ABM ÁLBUM")
        console.print(Align.center(tabla_principal))

        tabla_opcion = Table(expand=True, style="orange_red1", box=box.DOUBLE_EDGE, show_header=False)
        tabla_opcion.add_row("[cyan bold]1[/] - [bold]ALTA DE ÁLBUM[/]")
        tabla_opcion.add_row("[cyan bold]2[/] - [bold]BAJA DE ÁLBUM[/]")
        tabla_opcion.add_row("[cyan bold]3[/] - [bold]MODIFICACIÓN DE ÁLBUM[/]")
        tabla_opcion.add_row("[cyan bold]4[/] - [bold italic red1]SALIR[/]") 
        console.print(tabla_opcion)

        try:
            if incorrecto_abm == 1:
                tabla_incorrecto = Table(expand=True, style="red1", box=box.ASCII, show_header=False)
                tabla_incorrecto.add_row("[i]¡Opción [bold red1]incorrecta[/]![/i] :flushed:")
                console.print(tabla_incorrecto)

            if valuerror_abm == 1:
                tabla_error = Table(expand=True, style="red1", box=box.ASCII, show_header=False)
                tabla_error.add_row("[i]Ingrese solo [bold red1]números[/], por favor[/i] :confused:.")
                console.print(tabla_error)
            
            tabla_op = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False)
            tabla_op.add_row("[i]Ingrese su [bold cyan]opción[/][/i] :smiley:: ")
            console.print(tabla_op)
            opcion = int(console.input("[bold cyan]>: "))
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
            controlador.EliminarAlbum()
        elif opcion == 3:
            controlador.ModificarAlbum()
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

    console.rule("", style="bold gold3")
    console.print("DISQUERÍA FORMOSA MUSICAL", justify="center", style="bold white on deep_sky_blue4")
    console.rule("", style="bold gold3")

    tabla_principal = Table(box=box.ROUNDED, show_header=False, style="bold gold3")
    tabla_principal.add_row("[bold gold3]MENÚ PRINCIPAL")
    console.print(Align.center(tabla_principal))

    tabla_opcion = Table(expand=True, style="deep_sky_blue3", box=box.DOUBLE_EDGE, show_header=False)
    tabla_opcion.add_row("[cyan bold]1[/] - [bold]ALTA, BAJA O MODIFICACIÓN DE UN ÁLBUM[/]")
    tabla_opcion.add_row("[cyan bold]2[/] - [bold]LISTADO DE ÁLBUMES POR ARTISTAS[/]")
    tabla_opcion.add_row("[cyan bold]3[/] - [bold]LISTADO DE ÁLBUMES POR GÉNERO MUSICAL[/]")
    tabla_opcion.add_row("[cyan bold]4[/] - [bold]BÚSQUEDA POR NOMBRE DE ÁLBUM[/]")
    tabla_opcion.add_row("[cyan bold]5[/] - [bold]ALTA, BAJA O MODIFICACIÓN DE INTÉRPRETE[/]") # EXTRA
    tabla_opcion.add_row("[cyan bold]6[/] - [bold italic red1]SALIR[/]") 
    console.print(tabla_opcion)

    try:
        if incorrecto == 1:
            tabla_incorrecto = Table(expand=True, style="red1", box=box.ASCII, show_header=False)
            tabla_incorrecto.add_row("[i]¡Opción [bold red1]incorrecta[/]![/i] :flushed:")
            console.print(tabla_incorrecto)

        if valuerror == 1:
            tabla_error = Table(expand=True, style="red1", box=box.ASCII, show_header=False)
            tabla_error.add_row("[i]Ingrese solo [bold red1]números[/], por favor[/i] :confused:.")
            console.print(tabla_error)
        
        tabla_op = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False)
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
        ABMAlbum()
    elif opcion == 2:
        barra_progreso()
        controlador.ListarAlbumesPorArtistas()
    elif opcion == 3:
        barra_progreso()
        controlador.ListarAlbumesPorGenero()
    elif opcion == 4:
        None
    elif opcion == 5:
        ABMInterprete()
    elif opcion == 6:
        console.print("\n[italic bold]¡[gold1]Gracias[/], nos vemos![/] :sunglasses:\n")
        break

    # Resetear bandera para el regreso:
    incorrecto = 0
    valuerror = 0