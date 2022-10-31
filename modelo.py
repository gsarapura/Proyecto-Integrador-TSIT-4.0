from ast import Break
import mysql.connector

from rich.console import Console
from rich.table import Table

class Conectar():
    console = Console(width=100)

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'disqueria'
            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)
    
    def ObtenerIDGenerado(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT @@identity as id"
                cursor.execute(sentenciaSQL)
                resultado = cursor.fetchall()
                self.conexion.commit()
                self.conexion.close()
                return resultado[0][0]
            except mysql.connector.Error as descripcionError:
                print("Error al obtener el ID generado!",descripcionError)

    def ListarAlbumes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT interprete.apellido, interprete.nombre, cod_album, album.nombre, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album INNER JOIN interprete ON album.id_interprete = interprete.id_interprete INNER JOIN discografica ON album.id_discografica = discografica.id_discografica INNER JOIN formato ON album.id_formato = formato.id_formato INNER JOIN genero ON album.id_genero = genero.id_genero WHERE album.vigente = 1 AND cantidad > 0 ORDER By interprete.apellido, interprete.nombre, cod_album"
                # Código Hernán:
                # senteciaSQL = "SELECT cod_album, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album, interprete, discografica,formato,genero WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero and album.vigente = 1 ORDER By interprete.apellido desc"
                # el vigente = 1 es para que no me traiga los que estan eliminados (vigente = 0)
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡Error al buscar!",descripcionError)

    def ListarPorGenero(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT genero.nombre,cod_album, album.nombre, interprete.apellido, interprete.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album INNER JOIN interprete ON album.id_interprete = interprete.id_interprete INNER JOIN discografica ON album.id_discografica = discografica.id_discografica INNER JOIN formato ON album.id_formato = formato.id_formato INNER JOIN genero ON album.id_genero = genero.id_genero WHERE album.vigente = 1  ORDER By genero.nombre asc, interprete.apellido, interprete.nombre"
                # Código Hernán:
                # senteciaSQL = "SELECT cod_album, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album, interprete, discografica,formato,genero WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero and album.vigente = 1 ORDER By genero.nombre asc"
                # el vigente = 1 es para que no me traiga los que estan eliminados
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡Error al buscar!",descripcionError)

    def ListarInterprete(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from interprete where vigente = 1" # el 1 espara que no me tragia los que estan eliminados
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡Error al buscar!",descripcionError)

    def InsertarInterprete(self,interprete):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                revisoExistenciaSQL = "SELECT * from interprete where nombre = %s and apellido = %s "
                data = (interprete.getNombre(),interprete.getApellido())
                cursor.execute(revisoExistenciaSQL,data)
                resultado = cursor.fetchall()
                id = 0
                if len(resultado) == 0:
                    sentenciaSQL = "INSERT into interprete values(null,%s,%s,%s,%s,1)"
                    data = (interprete.getNombre(),interprete.getApellido(),interprete.getNacionalidad(),interprete.getFoto())
                    cursor.execute(sentenciaSQL,data)
                    id = self.ObtenerIDGenerado()
                    self.console.print("[i]Intérprete insertado [bold green3]correctamente[/][/i] :smiley:",justify="center")
                    # self.conexion.commit() # no hace falta porque ya se cierra al obtener el id generado
                    # self.conexion.close()
                else:
                    print("El intérprete ya existe")
                    option = input("¿Desea darlo de alta nuevamente? (Si/No): ")
                    option = option.lower()
                    if option == "si":
                        sentenciaSQL = "update interprete set vigente = 1 where nombre = %s and apellido = %s"
                        data = (interprete.getNombre(),interprete.getApellido())
                        cursor.execute(sentenciaSQL,data)
                        traerId = "Select id_interprete from interprete where nombre = %s and apellido = %s limit 1"
                        cursor.execute(traerId,data)
                        id = cursor.fetchall()
                        id = id[0][0]
                        self.conexion.commit()
                        self.conexion.close()
                        print("Intérprete dado de alta nuevamente")
                    else:
                        print("Intérprete no dado de alta nuevamente")
                        self.conexion.commit()
                        self.conexion.close()
                return id if id != 0 else 0
            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al Guardar![/i]", descripcionError)

    def ModificarInterprete(self,interprete):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "update interprete set nombre = %s, apellido = %s, nacionalidad = %s, foto = %s where id_interprete = %s"

                data = (interprete.getNombre(),interprete.getApellido(),interprete.getNacionalidad(),interprete.getFoto(),interprete.getId_Interprete())

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                
                self.console.print("[i]Intérprete modificado [bold green3]correctamente[/][/i] :smiley:",justify="center")

            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al modificar![/i]", descripcionError)

    def EliminarInterprete(self,id_interprete):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                # cursor = self.conexion.cursor(buffered=True)
                revisoAlbumsSQL = "select * from album where id_interprete = %s and vigente = 1"
                cursor.execute(revisoAlbumsSQL,(id_interprete,))
                resultados = cursor.fetchall()
                if len(resultados) > 0:
                    self.console.print("[i][bold red1]No[/] se puede eliminar el interprete porque hay álbumes y temas asociados a ese Id[/i][bold red1]: ")
                    #Table
                    table = Table(title="Interprete")
                    table.add_column("ID", style="cyan",justify="center")
                    table.add_column("COD. ÁLBUM", style="cyan", justify="center")
                    table.add_column("NOMBRE", style="cyan", justify="center")
                    table.add_column("ID INTÉR.", style="cyan", justify="center")
                    table.add_column("ID GÉN.", style="cyan", justify="center")
                    table.add_column("CANT. TEMAS", style="cyan", justify="center")
                    table.add_column("ID DISCO.", style="cyan", justify="center")
                    table.add_column("ID FORMATO", style="cyan", justify="center")
                    table.add_column("FECHA", style="cyan", justify="center")
                    table.add_column("PRECIO", style="cyan", justify="center")
                    table.add_column("CANTIDAD", style="cyan", justify="center")
                    for i in resultados:
                        table.add_row(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5]), str(i[6]), str(i[7]), str(i[8]), str(i[9]), str(i[10]))
                    self.console.print(table)

                    option = self.console.input("[i]¿Desea [bold red1]dar de baja[/] los álbumes y temas asociados a ese intérprete? [bold cyan]Si[/]/[bold red1]No[/][/i][bold cyan]: ")
                    option = option.lower()
                    if  option == "si":
                        sentenciaSQL = "update album set vigente = 0 where id_interprete = %s;"
                        sentenciaSQL2 = "update tema set vigente = 0 where id_album in (select id_album from album where id_interprete = %s)"
                        cursor.execute(sentenciaSQL,(id_interprete,))
                        cursor.execute(sentenciaSQL2,(id_interprete,))
                        self.conexion.commit()
                        self.conexion.close()
                        self.console.print("[i]Albunes [bold red1]eliminados[/] correctamente[/i]")
                    else:
                        self.console.print("[i][bold red1]No[/] se eliminaron los álbumes ni el intérprete[/i]")
                        self.conexion.commit()
                        self.conexion.close()
                else:
                    sentenciaSQL = "update interprete set vigente = 0 where id_interprete = %s"
                    #El 0 es para darlo de baja de manera lógica
                    data = (id_interprete,)

                    cursor.execute(sentenciaSQL,data)

                    self.conexion.commit()
                    self.conexion.close()
                   
                    self.console.print("[i]Intérprete eliminado [bold green3]correctamente[/][/i] :smiley:",justify="center")

            except mysql.connector.Error as descripcionError:
                print("Error al Eliminar!",descripcionError)
                self.console.print("[i]¡[bold red1]Error[/] al eliminar![/i]", descripcionError)

    def InsertarGenero(self,nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into genero values(null,%s)"

                data = (nombre,)

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Género insertado correctamente")

            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al guardar![/i]", descripcionError)

    def InsertarAlbum(self,album):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "insert into album values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1);"

                data = (album.getCod_album(),
                album.getNombre(),
                album.getId_interprete(),
                album.getId_genero(),
                album.getCant_temas(),
                album.getId_discografica(),
                album.getId_formato(),
                album.getFec_lanzamiento(),
                album.getPrecio(),
                album.getCantidad(),
                album.getCaratula())

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                self.console.print("[i]Álbum insertado [bold green3]correctamente[/][/i] :smiley:",justify="center")

            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al guardar![/i]", descripcionError)

    
    def ModificarAlbum(self,album):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE album SET nombre = %s, id_interprete = %s, id_genero = %s, cant_temas = %s, id_discografica = %s, id_formato = %s, fec_lanzamiento = %s, precio = %s, cantidad = %s, caratula = %s WHERE cod_album = %s AND vigente = 1"

                data = (album.getNombre(),
                album.getId_interprete(),
                album.getId_genero(),
                album.getCant_temas(),
                album.getId_discografica(),
                album.getId_formato(),
                album.getFec_lanzamiento(),
                album.getPrecio(),
                album.getCantidad(),
                album.getCaratula(),
                album.getCod_album())

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()

                self.console.print("[i]Álbum modificado [bold green3]correctamente[/][/i] :smiley:",justify="center")

            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al modificar![/i]", descripcionError)
    
    def EliminarAlbum(self,cod_album):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                revisoTemasSQL = "SELECT * FROM tema inner join album on tema.id_album = album.id_album where album.cod_album = %s AND tema.vigente = 1"
                # Hernán:
                #"select * from album where cod_album = %s and vigente = 1"
                cursor.execute(revisoTemasSQL,(cod_album,))
                resultados = cursor.fetchall()
                if len(resultados) > 0:
                    self.console.print("[i][bold red1]No[/] se puede eliminar el álbum porque hay temas asociados a ese id[/i][bold red1]: ")
                    #Table
                    table = Table(title="Temas")
                    table.add_column("ID", style="cyan",justify="center")
                    table.add_column("TÍTULO", style="cyan", justify="center")
                    table.add_column("DURACIÓN", style="cyan", justify="center")
                    table.add_column("AUTOR", style="cyan", justify="center")
                    table.add_column("COMPOSITOR", style="cyan", justify="center")
                    for i in resultados:
                        table.add_row(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]))
                    self.console.print(table)

                    self.console.rule("", style="bold orange_red1")
                    option = self.console.input("[i]¿Desea [bold red1]dar de baja[/] los temas asociados a ese álbum? [bold cyan]Si[/]/[bold red1]No[/][/i][bold cyan]: ")
                    option = option.lower()
                    if option == "si":
                        sentenciaSQL = "update tema inner join album on tema.id_album = album.id_album set tema.vigente = 0 where album.cod_album = %s"
                        # Hernan
                        # update tema set vigente = 0 where cod_album = %s
                        cursor.execute(sentenciaSQL,(cod_album,))
                        self.conexion.commit()
                        self.conexion.close()
                        self.console.print("[i]Temas eliminados [bold green3]correctamente[/][/i] :smiley:",justify="center")
                        return
                    else:
                        self.conexion.commit()
                        self.conexion.close()
                        self.console.print("[i][bold green3]No[/] se han efectuado cambios[/i].",justify="center")
                        return
                else:
                    sentenciaSQL = "UPDATE  album set vigente = 0 WHERE cod_album = %s" 
                    #Al poner el vigente en 0 lo elimino de manera lógica, yaque los select filtrarán por vigente = 1

                    data = (cod_album,)

                    cursor.execute(sentenciaSQL,data)

                    self.conexion.commit()
                    self.conexion.close()
                    self.console.print("[i]Álbum eliminado [bold green3]correctamente[/][/i] :smiley:",justify="center")

            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al eliminar![/i]", descripcionError)
    
    def ListarTema(self):
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from tema where vigente = 1" # el 1 espara que no me tragia los que estan eliminados
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al buscar![/i]", descripcionError)

    def ListarGenero(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from genero where vigente = 1" # el 1 espara que no me tragia los que estan eliminados
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.commit()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al buscar![/i]", descripcionError)

    def ListarDiscografica(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from discografica where vigente = 1" # el 1 espara que no me tragia los que estan eliminados
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                self.console.print("[i]¡[bold red1]Error[/] al buscar![/i]", descripcionError)

    def ListarFormato(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from formato where vigente = 1" # el 1 espara que no me tragia los que estan eliminados
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡Error al Buscar!",descripcionError)
    
    def ListarBusquedaNombreAlbum(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = """SELECT album.cod_album, album.nombre, interprete.apellido, interprete.nombre, genero.nombre, discografica.nombre, album.fec_lanzamiento, album.precio, album.cantidad, formato.tipo
                FROM album 
                INNER JOIN interprete ON album.id_interprete = interprete.id_interprete
                INNER JOIN discografica ON album.id_discografica = discografica.id_discografica 
                INNER JOIN formato ON album.id_formato = formato.id_formato 
                INNER JOIN genero ON album.id_genero = genero.id_genero
                WHERE album.nombre like %s
                AND album.vigente = 1"""

                cursor.execute(sentenciaSQL, (('%' + nombre + '%',)))
                resultados = cursor.fetchall()

                self.conexion.commit()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡Ha ocurrido un error! Intente nuevamente.", descripcionError)


    def ExistenciaId (self,id,tabla):
        if self.conexion.is_connected():
            try:
                if(id == '' or id == ' '):
                    return False
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM "+tabla+" WHERE vigente = 1 AND id_"+tabla+" = %s"
                cursor.execute(sentenciaSQL,(id,))
                resultados = cursor.fetchall()
                self.conexion.commit()
                # self.conexion.close() Cerramos conexión dentro de la función que llama a esta.                
                if len(resultados) == 0:
                    return False
                else:
                    return True
            except mysql.connector.Error as descripcionError:
                print("¡Ha ocurrido un error! Intente nuevamente.", descripcionError)

    def ExistenciaCod (self,id,tabla):
        if self.conexion.is_connected():
            try:
                if(id == '' or id == ' '):
                    return False
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM album WHERE vigente = 1 AND cod_album = %s"
                cursor.execute(sentenciaSQL,(id,))
                resultados = cursor.fetchall()
                # self.conexion.commit()
                # self.conexion.close()                
                if len(resultados) == 0:
                    return False
                else:
                    return True
            except mysql.connector.Error as descripcionError:
                print("¡Ha ocurrido un error! Intente nuevamente.", descripcionError)
    def SalirOpcion(self):
        self.console.print("[i]¡[bold red1]Saliendo[/] del programa![/i]", justify="center")
        return Break()

#------------------------------------------------------------------------------------------------------
class Interprete():     

    def __init__(self,id_interprete,nombre,apellido,nacionalidad,foto,vigente) -> None:
        self.id_interprete = id_interprete
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.foto = foto
        self.vigente = vigente
    def getId_Interprete(self):
        return self.id_interprete
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getNacionalidad(self):
        return self.nacionalidad
    def getFoto(self):
        return self.foto

    def setId_Interprete(self,idInterprete):
        self.id_interprete = idInterprete
    def setNombre(self,nombre):
        self.nombre = nombre
    def setApellido(self,apellido):
        self.apellido = apellido
    def setNacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad
    def setFoto(self,foto):
        self.foto = foto

    def __str__(self) -> str:
        return str(self.id_interprete)+' '+self.nombre+' '+self.apellido+' '+self.nacionalidad+' '+self.foto

#---------------------------------------------------------------------------------------

class Genero():
    def __init__(self,id_genero,nombre,vigente) -> None:
        self.id_genero = id_genero
        self.nombre = nombre
        self.vigente = vigente
    def __str__(self) -> str:
        return str(self.id_genero)+' '+self.nombre

    def getId_genero(self):
        return self.getId_genero
    def getNombre(self):
        return self.nombre

    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setNombre(self,nombre):
        self.nombre = nombre


#---------------------------------------------------------------------------------------

class Discografica():
    def __init__(self,id_discografica,nombre,vigente) -> None:
        self.id_discografica = id_discografica
        self.nombre = nombre
        self.vigente = vigente

    def __str__(self) -> str:
        return str(self.id_discografica)+' '+self.nombre

    def getId_discografica(self):
        return self.id_discografica
    def getNombre(self):
        return self.nombre
    
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setNombre(self,nombre):
        self.nombre = nombre


#---------------------------------------------------------------------------------------

class Formato():
    def __init__(self,id_formato,tipo,vigente) -> None:
        self.id_formato = id_formato
        self.tipo = tipo
        self.vigente = vigente

    def __str__(self) -> str:
        return str(self.id_formato)+' '+self.tipo

    def getId_formato(self):
        return self.id_formato
    def getTipo(self):
        return self.tipo
    def getVigente(self):
        return self.vigente

    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setTipo(self,tipo):
        self.tipo = tipo
    def setVigente(self,vigente):
        self.vigente = vigente
#---------------------------------------------------------------------------------------

class Tema():
    def __init__(self,id_tema,titulo,duracion,autor,compositor,cod_album,id_interprete,vigente) -> None:
        self.id_tema = id_tema
        self.titulo = titulo
        self.duracion = duracion
        self.autor = autor
        self.compositor = compositor
        self.cod_album = cod_album
        self.id_interprete = id_interprete
        self.vigente = vigente

    def getId_tema(self):
        return self.id_tema
    def getTiulo(self):
        return self.titulo
    def getDuracion(self):
        return self.duracion
    def getAutor(self):
        return self.autor
    def getCompositor(self):
        return self.compositor
    def getCod_album(self):
        return self.cod_album
    def getId_interprete(self):
        return self.id_interprete
    def getVigente(self):
        return self.vigente

    def setId_tema(self,id_tema):
        self.id_tema = id_tema
    def setTitulo(self,titulo):
        self.titulo = titulo
    def setDuracion(self,duracion):
        self.duracion = duracion
    def setAutor(self,autor):
        self.autor = autor
    def setCompositor(self,compositor):
        self.compositor = compositor
    def setCod_album(self,cod_album):
        self.cod_album = cod_album
    def setId_interprete(self,id_interprete):
        self.id_interprete = id_interprete
    def setVigente(self,vigente):
        self.vigente = vigente


    def __str__(self) -> str:
        return str(self.id_tema)+' '+self.titulo+' '+str(self.duracion)+' '+self.autor+' '+self.compositor+' '+str(self.cod_album)+' '+str(self.id_interprete)+ ' '+str(self.vigente)
    


#---------------------------------------------------------------------------------------

class Album():
    def __init__(self,id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula,vigente) -> None:
        self.id_album = id_album
        self.cod_album = cod_album
        self.nombre = nombre
        self.id_interprete = id_interprete
        self.id_genero = id_genero
        self.cant_temas = cant_temas
        self.id_discografica = id_discografica
        self.id_formato = id_formato
        self.fec_lanzamiento = fec_lanzamiento
        self.precio = precio
        self.cantidad = cantidad
        self.caratula = caratula
        self.vigente = vigente
    def getId_album(self):
        return self.id_album
    def getCod_album(self):
        return self.cod_album
    def getNombre(self):
        return self.nombre
    def getId_interprete(self):
        return self.id_interprete
    def getId_genero(self):
        return self.id_genero
    def getCant_temas(self):
        return self.cant_temas
    def getId_discografica(self):
        return self.id_discografica
    def getId_formato(self):
        return self.id_formato
    def getFec_lanzamiento(self):
        return self.fec_lanzamiento
    def getPrecio(self):
        return self.precio
    def getCantidad(self):
        return self.cantidad
    def getCaratula(self):
        return self.caratula
    def getVigente(self):
        return self.vigente

    def setId_album(self,id_album):
        self.id_album = id_album
    def setCod_album(self,cod_album):
        self.cod_album = cod_album
    def setNombre(self,nombre):
        self.nombre = nombre
    def setId_interprete(self,id_interprete):
        self.id_interprete = id_interprete
    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setCant_temas(self,cant_temas):
        self.cant_temas = cant_temas
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setFec_lanzamiento(self,fec_lanzamiento):
        self.fec_lanzamiento = fec_lanzamiento
    def setPrecio(self,precio):
        self.precio = precio
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    def setCaratula(self,caratula):
        self.caratula = caratula
    def setVigente(self,vigente):
        self.vigente = vigente
    def __str__(self) -> str:
        return str(self.id_album) +' '+ str(self.cod_album) +' '+ self.nombre +' '+ str(self.id_interprete) +' '+ str(self.id_genero) +' '+ str(self.cant_temas) +' '+ str(self.id_discografica) +' '+ str(self.id_formato) +' '+ self.fec_lanzamiento +' '+ str(self.precio) +' '+ str(self.cantidad) +' '+ self.caratula + ' ' + str(self.vigente)

    

    #---------------------------------------------------------------------------------------------------------

AComoAmor = Album(0,456783,'A Como Amor',3,5,10,5,3,'1978-01-01',899.99,3,'',1)

#con = Conectar()
#con.InsertarAlbum(AComoAmor)
