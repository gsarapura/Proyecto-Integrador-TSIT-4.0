from ast import Break
import modelo
from datetime import datetime
# Módulos Rich:
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich import box

console = Console(width=100)

# Listar artistas, género, discográfica y formato
#---------------------------------------------------------------------------------------
def ListarArtistasVigentes():
    con = modelo.Conectar()
    table = Table(title="Estos son los intérpretes vigentes actualmente:")
    columnas = ["ID", "APELLIDO", "NOMBRE", "NACIONALIDAD", "URL FOTO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarInterprete():
        table.add_row(str(i[0]), str(i[2]), str(i[1]), str(i[3]), str(i[4]))

    console.print(Align.center(table))

def ListarGenero():
    con = modelo.Conectar()
    table = Table(title="Géneros:")
    columnas = ["ID", "NOMBRE"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarGenero():
        table.add_row(str(i[0]), str(i[1]))

    console.print(Align.center(table))

def ListarDiscografica():
    con = modelo.Conectar()
    table = Table(title="Discográfica:")
    columnas = ["ID", "NOMBRE"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarDiscografica():
        table.add_row(str(i[0]), str(i[1]))

    console.print(Align.center(table))

def ListarFormato():
    con = modelo.Conectar()
    table = Table(title="Formato:")
    columnas = ["ID", "TIPO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarFormato():
        table.add_row(str(i[0]), str(i[1]))

    console.print(Align.center(table))

# Listar álbums
#---------------------------------------------------------------------------------------
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
    console = Console()
    console.print(table)    

def ListarBusquedaNombreAlbum():
    con = modelo.Conectar()

    tabla_busqueda = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False)
    tabla_busqueda.add_row("[i]Ingrese el [bold cyan]nombre del álbum[/][/i] que desea buscar: ")
    console.print(tabla_busqueda)

    # Asegurar que ingrese un valor. 
    nombre = ""
    while nombre == "":
        nombre = console.input("[bold cyan]>: ")
        if nombre == "":
            console.rule("", style="bold red1")
            console.print("[i]Por favor, ingrese [bold green3]nombre del álbum[/][/i]: ")
        
    coincidencias = con.ListarBusquedaNombreAlbum(nombre)

    table = Table(title="Albumes coincidentes: ")
    columnas = ["COD. ÁLBUM", "NOMBRE", "APELLIDO ART.", "NOMBRE ART.", "GÉNERO", "DISCOGRÁFICA", "FECHA LANZAMIENTO", "PRECIO", "CANTIDAD", "FORMATO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    if len(coincidencias) == 0:
        console.print("[i][bold red1]No[/] se encontraron coincidencias[/i]. :x:", justify="center")
        return

    for album in coincidencias:
        table.add_row(str(album[0]), str(album[1]), str(album[2]), str(album[3]), str(album[4]), str(album[5]), str(album[6]), str(album[7]), str(album[8]), str(album[9]))
    consola = Console()
    consola.print(table)
    return

# Validaciones
#---------------------------------------------------------------------------------------
def validar_entero(dato):
    while True:
        if dato.isdigit():
            return dato
        else:
            dato = console.input("[i]Por favor, ingrese [bold green3]enteros[/][bold]:[/i] ")
            console.rule("", style="bold red1")

# ABM álbums
#---------------------------------------------------------------------------------------
def InsertarAlbum():
    # Abrir conexión
    con = modelo.Conectar()
    
    console.print("[i][bold orange_red1]----[/] Para volver al menú escriba [bold red1]salir[/] [bold orange_red1]----[/][/i]", justify="center")  
    console.rule("", style="bold orange_red1")
    cod_album = (console.input("[i]Ingrese el [cyan bold]código[/] del álbum[/i][bold cyan]: "))
    
    # Salida
    if cod_album.lower() == "salir":
        return Break()
    
    # Verificar cod sea entero con recursión
    try:
        cod_album = int(cod_album)
    except: 
        console.print("[i]El código debe ser un [bold green3]número entero[/].[/i]")
        return InsertarAlbum() 
    
    # Nombre
    console.rule("", style="bold orange_red1")
    nombre = console.input("[i]Ingrese el [cyan bold]nombre[/] del álbum[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")


    ListarArtistasVigentes()

    console.rule("", style="bold orange_red1")
    console.print("[i]En caso de que el intérprete [bold red1]no[/] esté en la lista, [bold cyan]ingrese 0[/] para agregarlo.[/i]")  
    id_interprete = (console.input("[i]Ingrese el [bold cyan]ID[/] del intérprete[/i][bold cyan]: "))
    # Opción de ingresar intérprete
    id_interprete = InsertarInterprete() if id_interprete == "0" else id_interprete # Hago una Operación Ternaria para que el ListarGenero() sí se ejecute.
    console.rule("", style="bold orange_red1")
    # Verificar que sea válido
    while True:
        id_interprete = InsertarInterprete() if id_interprete == "0" else id_interprete # Hago una Operación Ternaria para que el ListarGenero() sí se ejecute.
        if con.ExistenciaId(id_interprete, "interprete"):
            break # Se sale del bucle cuando existe ID
        id_interprete = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")

    #while con.ExistenciaId(id_interprete, "interprete") == False:
    #    id_interprete = InsertarInterprete() if id_interprete == "0" else id_interprete # Hago una Operación Ternaria para que el ListarGenero() sí se ejecute.
    #    id_interprete = console.input("[i]Por favor, [bold cyan]ingrese un ID[/] válido[/i]: ")
    #    console.rule("", style="bold red1")

    ListarGenero()
    console.rule("", style="bold orange_red1")
    id_genero = (console.input("[i]Ingrese el [bold cyan]ID[/] del género[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    while con.ExistenciaId(id_genero, "genero") == False:
        id_genero = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: " )
        console.rule("", style="bold red1")
  
    # Verificar que cant_temas sea un entero:
    cant_temas = console.input("[i]Ingrese la [bold cyan]cantidad[/] de temas[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")
    cant_temas = validar_entero(cant_temas)

    ListarDiscografica()
    console.rule("", style="bold orange_red1")
    id_discografica = (console.input("[i]Ingrese el [bold cyan]ID[/] de la discografica[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    while con.ExistenciaId(id_discografica, "discografica") == False:
        id_discografica = console.input("[i][i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")
        

    ListarFormato()
    console.rule("", style="bold orange_red1")
    id_formato = (console.input("[i]Ingrese el [bold cyan]ID[/] del formato[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    while con.ExistenciaId(id_formato, "formato") == False:
        id_formato = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")
    
    fec_lanzamiento = console.input("[i]Ingrese la [bold cyan]fecha de lanzamiento[/] (aaaa-mm-dd)[bold cyan]: ")
    formato = "%Y-%m-%d"
    console.rule("", style="bold orange_red1")
    # Validar formato de fecha:
    while True:
        try:
            if bool(datetime.strptime(fec_lanzamiento, formato)):
                break
        except:
            fec_lanzamiento = console.input("[i]Por favor, ingrese el formato de fecha [bold green3]aaaa-mm-dd[/i][/]: ")
            console.rule("", style="bold red1")
   

    precio = console.input("[i]Ingrese el [bold cyan]precio[/][/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")
    precio = validar_entero(precio)
            
    cantidad = (console.input("[i]Ingrese [bold cyan]cantidad disponible[/] de este álbum[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    cantidad = validar_entero(cantidad)

    caratula = console.input("[i]Ingrese la [bold cyan]dirección web[/] de la Carátula[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula,1)
    con.InsertarAlbum(nuevoAlbum)

def ModificarAlbum():
    con = modelo.Conectar()

    ListarAlbumesPorArtistas()
    console.print("[i][bold orange_red1]----[/] Para volver al menú escriba [bold red1]salir[/] [bold orange_red1]----[/][/i]", justify="center")  
    console.rule("", style="bold orange_red1")  

    cod_album = (console.input("[i]Ingrese el código del [bold cyan]álbum[/] que quiere modificar[/i][bold cyan]: "))
    if cod_album.lower() == "salir":
        return Break()
    console.rule("", style="bold orange_red1")
    while con.ExistenciaCod(cod_album, "album") == False:
        cod_album = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")


    nombre = console.input("[i]Ingrese el [bold cyan]nuevo nombre[/] del álbum[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")

    # Hay que tener los siguientes datos ya dentro de la base:

    ListarArtistasVigentes()
    console.rule("", style="bold orange_red1")
    id_interprete = console.input("[i]Ingrese el [bold cyan]ID[/] del intérprete[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")
    while con.ExistenciaId(id_interprete, "interprete") == False:
        id_interprete = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")

    ListarGenero()
    console.rule("", style="bold orange_red1")
    id_genero = console.input("[i]Ingrese el [bold cyan]ID[/] del Género[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")
    while con.ExistenciaId(id_genero, "genero") == False:
        id_genero = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")

    cant_temas = console.input("[i]Ingrese la [bold cyan]cantidad[/] de temas[/i][bold cyan]: ") # Menos este, por supuesto.
    console.rule("", style="bold orange_red1")
    cant_temas = validar_entero(cant_temas)

    ListarDiscografica()
    console.rule("", style="bold orange_red1")
    id_discografica = console.input("[i]Ingrese el [bold cyan]ID[/] de la discografica[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")
    while con.ExistenciaId(id_discografica, "discografica") == False:
        id_discografica = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")    

    ListarFormato()
    console.rule("", style="bold orange_red1")
    id_formato = console.input("[i]Ingrese el [bold cyan]ID[/] del formato[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")
    while con.ExistenciaId(id_formato, "formato") == False:
        id_formato = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")
    
    # Hasta acá.
    fec_lanzamiento = console.input("[i]Ingrese la [bold cyan]fecha de lanzamiento[/] (aaaa-mm-dd)[bold cyan]: ")
    formato = "%Y-%m-%d"
    console.rule("", style="bold orange_red1")
    # Validar formato de fecha:
    while True:
        try:
            if bool(datetime.strptime(fec_lanzamiento, formato)):
                break
        except:
            fec_lanzamiento = console.input("[i]Por favor, ingrese el formato de fecha [bold green3]aaaa-mm-dd[/i][/]: ")
            console.rule("", style="bold red1")
    
    precio = (console.input("[i]Ingrese el [bold cyan]precio[/][/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    precio = validar_entero(precio)

    cantidad = (console.input("[i]Ingrese [bold cyan]cantidad disponible[/] de este álbum[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    cantidad = validar_entero(cantidad)

    caratula = console.input("[i]Ingrese la [bold cyan]dirección web[/] de la carátula[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula,1)
    con.ModificarAlbum(nuevoAlbum)
    
def EliminarAlbum():
    con = modelo.Conectar()
    ListarAlbumesPorArtistas()
    console.print("[i][bold orange_red1]----[/] Para volver al menú escriba [bold red1]salir[/] [bold orange_red1]----[/][/i]", justify="center")  
    console.rule("", style="bold orange_red1")

    cod_album = (console.input("[i]Ingrese el [bold cyan]código del Álbum[/] que quiere eliminar[/i][bold cyan]: "))
    if cod_album.lower() == "salir":
        return Break()
    console.rule("", style="bold orange_red1")

    while con.ExistenciaCod(cod_album, "album") == False:
        cod_album = console.input("[i]Por favor, ingrese un [bold green3]código válido[/][/i]: ")
        console.rule("", style="bold red1")

    con.EliminarAlbum(cod_album)

# ABM intérpretes
#---------------------------------------------------------------------------------------
def InsertarInterprete():
    console.print("[i][bold orange_red1]----[/] Para volver al menú escriba [bold red1]salir[/] [bold orange_red1]----[/][/i]", justify="center")  

    datos = ["el [cyan bold]nombre[/]", "el [cyan bold]apellido[/]", "la [cyan bold]nacionalidad[/]", "la [cyan bold]foto[/]"] 
    inputs = [] 
    for i in datos:
        console.rule("", style="bold orange_red1")
        inputs.append(console.input("[i]Ingrese "+ i +" del intérprete[/i][bold cyan]: "))
        if inputs[-1].lower() == "salir":
            return Break()
    console.rule("", style="bold orange_red1")
    
    nuevoInterprete = modelo.Interprete(0, inputs[0], inputs[1], inputs[2], inputs[3], 1)#El 1 es para darlo de alta en vigente. Si el vigente es 0 (false) no se mostrará.
    con = modelo.Conectar()
    return con.InsertarInterprete(nuevoInterprete) 

def ModificarInterprete():
    ListarArtistasVigentes()
    console.print("[i][bold orange_red1]----[/] Para volver al menú escriba [bold red1]salir[/] [bold orange_red1]----[/][/i]", justify="center")   
    con = modelo.Conectar()

    datos = ["el [cyan bold]ID[/]", "el [cyan bold]nuevo nombre[/]", "el [cyan bold]nuevo apellido[/]", "la [cyan bold]nueva nacionalidad[/]", "la [cyan bold]nueva dirección web[/] de la foto"]
    inputs = []
    console.rule("", style="bold orange_red1")
    for i in datos:
        if i == "el [cyan bold]ID[/]":
            inputs.append(console.input("[i]Ingrese "+ i +" del intérprete que quiere modificar[/i][bold cyan]: "))

            if inputs[-1].lower() == "salir":
                return Break()
           
            # Verificar id
            while con.ExistenciaId(inputs[0], "interprete") == False:
                console.rule("", style="bold red1")
                inputs[0] = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
            
            continue
            
        console.rule("", style="bold orange_red1")
        inputs.append(console.input("[i]Ingrese "+ i +" del intérprete[/i][bold cyan]: "))

        if inputs[-1].lower() == "salir":
            return Break()
    
    console.rule("", style="bold orange_red1")
    nuevoInterprete = modelo.Interprete(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], 1)#el 1 es para que no se elimine... mantenerlo vigente   
    con.ModificarInterprete(nuevoInterprete)

def EliminarInterprete():
    con = modelo.Conectar()
    ListarArtistasVigentes()
    console.print("[i][bold orange_red1]----[/] Para volver al menú escriba [bold red1]salir[/] [bold orange_red1]----[/][/i]", justify="center")  
    console.rule("", style="bold orange_red1")

    id_interprete = (console.input("[i]Ingrese el [bold cyan]ID[/] del intérprete que quiere eliminar[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    if id_interprete.lower() == "salir":
        return Break()
    while con.ExistenciaId(id_interprete, "interprete") == False:
        id_interprete = console.input("[i]Por favor, ingrese un [bold green3]ID válido[/][/i]: ")
        console.rule("", style="bold red1")
    
    con.EliminarInterprete(id_interprete)