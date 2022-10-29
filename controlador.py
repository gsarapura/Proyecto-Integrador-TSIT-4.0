import modelo
# Módulos Rich:
from rich.table import Table
from rich.console import Console
from rich import box
from rich.align import Align

console = Console(width=100)
    
def enter_continuar():
    console = Console(width=100)
    tabla_continuar = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False)
    tabla_continuar.add_row("[i]Presione [bold cyan]ENTER[/][/i] para continuar: ")
    console.print(tabla_continuar)
    console.input("[bold cyan]>: ")

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
 
    input("Presione ENTER para continuar")

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
    
    enter_continuar()

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

def tabla_artistas_vigentes():
    con = modelo.Conectar()
    # Rich
    table = Table(title="Estos son los Intérpretes vigentes actualmente:")
    columnas = ["ID", "APELLIDO", "NOMBRE", "NACIONALIDAD"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarInterprete():
        table.add_row(str(i[0]), str(i[2]), str(i[1]), str(i[3]))

    console.print(Align.center(table))

def InsertarInterprete():
    # Rich
    tabla_artistas_vigentes()
    
    datos = ["el [cyan bold]nombre[/]", "el [cyan bold]apellido[/]", "la [cyan bold]nacionalidad[/]", "la [cyan bold]foto[/]"] 
    inputs = []
    for i in datos:
        console.rule("", style="bold orange_red1")
        inputs.append(console.input("[i]Ingrese "+ i +" del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    nuevoInterprete = modelo.Interprete(0, inputs[0], inputs[1], inputs[2], inputs[3], 1)#El 1 es para darlo de alta en vigente. Si el vigente es 0 (false) no se mostrará.
    con = modelo.Conectar()
    con.InsertarInterprete(nuevoInterprete)
    enter_continuar()

def ModificarInterprete():
    tabla_artistas_vigentes()

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
    enter_continuar()

def EliminarInterprete():
    tabla_artistas_vigentes()
    
    console.rule("", style="bold orange_red1")
    id_interprete = int(console.input("[i]Ingrese el [bold cyan]ID [/] del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    con = modelo.Conectar()
    con.EliminarInterprete(id_interprete)
    enter_continuar()