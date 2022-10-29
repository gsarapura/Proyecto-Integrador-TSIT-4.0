import modelo
# Módulos Rich:
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich import box

console = Console(width=100)
    
def ListarAlbumesPorArtistas():
    con = modelo.Conectar()
    listado = con.ListarAlbumes()
    
    table = Table(title="Álbumes por Artistas")
    columnas = ["APELLIDO", "NOMBRE", "COD. ÁLBUM", "ÁLBUM", "GÉNERO", "DISCOGRÁFICA", "PRECIO", "CANTIDAD", "FORMATO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for album in listado:
        table.add_row(str(album[0]), str(album[1]), str(album[2]), str(album[3]), str(album[4]), str(album[5]), str(album[6]), str(album[7]), str(album[8]))
    console = Console()
    console.print(table)
 


def ListarAlbumesPorGenero():
    con = modelo.Conectar() 
    listado = con.ListarPorGenero()
    
    table = Table(title="Álbumes por Género")
    columnas = ["GÉNERO", "COD. ÁLBUM", "ÁLBUM", "APELLIDO ARTISTA", "NOMBRE ARTISTA", "DISCOGRÁFICA", "PRECIO", "CANTIDAD", "FORMATO"]
    for col in columnas:
        table.add_column(col, style="light_sea_green", justify="center")
    
    for album in listado:
        table.add_row(str(album[0]), str(album[1]), str(album[2]), str(album[3]), str(album[4]), str(album[5]), str(album[6]), str(album[7]), str(album[8]))
    console = Console(width=140)
    console.print(Align.center(table))    

def InsertarAlbum():
    cod_album = int(input("\nIngrese el código del nuevo Álbum: "))
    nombre = input("Ingrese el nombre del álbum: ")

    # Hay que tener los siguientes datos ya dentro de la base:
    con = modelo.Conectar()

    print("\nIntérpretes Disponibles:")

    for i in con.ListarInterprete():
        print(i)
    print("\n")
    print("En caso de que el Intérprete no esté en la lista, ingrese 0 para agregarlo.")  
  
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    if id_interprete == 0:
        nombre = input("Ingrese el nombre del Intérprete: ")
        apellido = input("Ingrese el apellido del Intérprete: ")
        nacionalidad = input("Ingrese la nacionalidad del Intérprete: ")
        foto = input("Ingrese la dirección web de la foto del Intérprete: ")
        nuevoInterprete = modelo.Interprete(0,nombre,apellido,nacionalidad,foto,1)
        con.InsertarInterprete(nuevoInterprete)
        id_interprete = con.ObtenerIDGenerado()
        print("El ID del Intérprete es: ",id_interprete)  
    print("\nGénero")
    for g in con.ListarGenero():
        print(g)
    id_genero = int(input("\nIngrese el ID del Género: "))

    cant_temas = int(input("\nIngrese la cantidad de temas: ")) # Menos este, por supuesto.

    print("\nDiscográfica")
    for d in con.ListarDiscografica():
        print(d)
    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\nFormato")
    for f in con.ListarFormato():
        print(f)
    id_formato = int(input("\nIngrese el ID del formato: "))
    # Hasta acá.

    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
    precio = float(input("\nIngrese el precio: "))
    cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula,1)
    con.InsertarAlbum(nuevoAlbum)
    input("Presione ENTER para continuar")

def ModificarAlbum():
    ListarAlbumesPorArtistas()
    cod_album = int(input("\nIngrese el código del Álbum que quiere modificar: "))

    nombre = input("Ingrese el nuevo nombre del álbum: ")

    # Hay que tener los siguientes datos ya dentro de la base:
    con = modelo.Conectar()

    print("\nIntérpretes Disponibles:")

    for i in con.ListarInterprete():
        print(i)
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    
    print("\nGénero")
    for g in con.ListarGenero():
        print(g)
    id_genero = int(input("\nIngrese el ID del Género: "))

    cant_temas = int(input("\nIngrese la cantidad de temas: ")) # Menos este, por supuesto.

    print("\nDiscográfica")
    for d in con.ListarDiscografica():
        print(d)
    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\nFormato")
    for f in con.ListarFormato():
        print(f)
    id_formato = int(input("\nIngrese el ID del formato: "))
    # Hasta acá.

    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
    precio = float(input("\nIngrese el precio: "))
    cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula,1)
    con.ModificarAlbum(nuevoAlbum)
    input("Presione ENTER para continuar")

def EliminarAlbum():
    ListarAlbumesPorArtistas()
    cod_album = int(input("\nIngrese el código del Álbum que quiere eliminar: "))
    con = modelo.Conectar()
    con.EliminarAlbum(cod_album)
    input("Presione ENTER para continuar")

def InsertarInterprete():
    datos = ["el [cyan bold]nombre[/]", "el [cyan bold]apellido[/]", "la [cyan bold]nacionalidad[/]", "la [cyan bold]foto[/]"] 
    inputs = []
    for i in datos:
        console.rule("", style="bold orange_red1")
        inputs.append(console.input("[i]Ingrese "+ i +" del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    nuevoInterprete = modelo.Interprete(0, inputs[0], inputs[1], inputs[2], inputs[3], 1)#El 1 es para darlo de alta en vigente. Si el vigente es 0 (false) no se mostrará.
    con = modelo.Conectar()
    con.InsertarInterprete(nuevoInterprete)

def ModificarInterprete():
    datos = ["el [cyan bold]ID[/]", "el [cyan bold]nuevo nombre[/]", "el [cyan bold]nuevo apellido[/]", "la [cyan bold]nueva nacionalidad[/]", "la [cyan bold]nueva dirección web[/] de la foto"]
    inputs = []
    for i in datos:
        console.rule("", style="bold orange_red1")
        if i == "el [cyan bold]ID[/]":
            inputs.append(console.input("[i]Ingrese "+ i +" del intérprete que quiere modificar[/i][bold cyan]: "))
            continue
        inputs.append(console.input("[i]Ingrese "+ i +" del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    nuevoInterprete = modelo.Interprete(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], 1)#el 1 es para que no se elimine... mantenerlo vigente
    con = modelo.Conectar()
    con.ModificarInterprete(nuevoInterprete)

def EliminarInterprete():
    console.rule("", style="bold orange_red1")
    id_interprete = int(console.input("[i]Ingrese el [bold cyan]ID [/] del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    con = modelo.Conectar()
    con.EliminarInterprete(id_interprete)


def ListarBusquedaNombreAlbum():
    con = modelo.Conectar()
    tabla_busqueda = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False)
    tabla_busqueda.add_row("[i]Ingrese el [bold cyan]nombre del álbum[/][/i] que desea buscar: ")
    console = Console()
    console.print(tabla_busqueda)
    nombre = console.input("[bold cyan]>: ")
    con = modelo.Conectar()
    print=" "
    print=" "
    print=" "
    print=" "

    table = Table(title="Albumes coincidentes: ")
    coincidencias = con.ListarBusquedaNombreAlbum(nombre)
    table.add_column("COD. ÁLBUM", style="cyan")
    table.add_column("NOMBRE", style="cyan")
    table.add_column("INTÉRPRETE", style="cyan")
    table.add_column("GÉNERO", style="cyan")
    table.add_column("DISCOGRÁFICA", style="cyan")
    table.add_column("PRECIO", style="cyan")
    table.add_column("CANTIDAD", style="cyan")
    table.add_column("FORMATO", style="cyan")
    table.add_column("FECHA", style="cyan")

    if len(coincidencias) == 0:
        print("No se encontraron coincidencias.")
        return
    for album in coincidencias:
        table.add_row(str(album[0]), str(album[1]), str(album[2]), str(album[3]), str(
            album[4]), str(album[5]), str(album[6]), str(album[7]), str(album[8]))
    
    console.print(table)
    return
