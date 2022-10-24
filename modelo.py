import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '15963200',
                db = 'disqueria'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)
    
    def ListarAlbumes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT interprete.apellido, interprete.nombre, cod_album, album.nombre, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album INNER JOIN interprete ON album.id_interprete = interprete.id_interprete INNER JOIN discografica ON album.id_discografica = discografica.id_discografica INNER JOIN formato ON album.id_formato = formato.id_formato INNER JOIN genero ON album.id_genero = genero.id_genero where cantidad>0 ORDER By interprete.apellido, interprete.nombre, cod_album"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados


            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)
    def ListarPorGenero(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT genero.nombre,cod_album, album.nombre, interprete.apellido, interprete.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album INNER JOIN interprete ON album.id_interprete = interprete.id_interprete INNER JOIN discografica ON album.id_discografica = discografica.id_discografica INNER JOIN formato ON album.id_formato = formato.id_formato INNER JOIN genero ON album.id_genero = genero.id_genero ORDER By genero.nombre asc, interprete.apellido, interprete.nombre"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados


            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ListarInterprete(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from interprete"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def InsertarInterprete(self,nombre,apellido,nacionalidad,foto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into interprete values(null,%s,%s,%s,%s)"

                data = (nombre,apellido,nacionalidad,foto)

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Intérprete insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

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
                print("¡No se conectó!",descripcionError)

    def InsertarAlbum(self,album):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "insert into album values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

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
                print("Álbum insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ListarTema(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from tema"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ListarGenero(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from genero"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ListarDiscografica(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from discografica"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

    def ListarFormato(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from formato"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                #self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError)

#------------------------------------------------------------------------------------------------------
class Interprete():     

    def __init__(self,id_interprete,nombre,apellido,nacionalidad,foto) -> None:
        self.id_interprete = id_interprete
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.foto = foto

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
    def __init__(self,id_genero,nombre) -> None:
        self.id_genero = id_genero
        self.nombre = nombre

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
    def __init__(self,id_discografica,nombre) -> None:
        self.id_discografica = id_discografica
        self.nombre = nombre

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
    def __init__(self,id_formato,tipo) -> None:
        self.id_formato = id_formato
        self.tipo = tipo

    def __str__(self) -> str:
        return str(self.id_formato)+' '+self.tipo

    def getId_formato(self):
        return self.id_formato
    def getTipo(self):
        return self.tipo

    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setTipo(self,tipo):
        self.tipo = tipo

#---------------------------------------------------------------------------------------

class Tema():
    def __init__(self,id_tema,titulo,duracion,autor,compositor,cod_album,id_interprete) -> None:
        self.id_tema = id_tema
        self.titulo = titulo
        self.duracion = duracion
        self.autor = autor
        self.compositor = compositor
        self.cod_album = cod_album
        self.id_interprete = id_interprete

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

    def __str__(self) -> str:
        return str(self.id_tema)+' '+self.titulo+' '+str(self.duracion)+' '+self.autor+' '+self.compositor+' '+str(self.cod_album)+' '+str(self.id_interprete)
    


#---------------------------------------------------------------------------------------

class Album():
    def __init__(self,id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula) -> None:
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

    def __str__(self) -> str:
        return str(self.id_album) +' '+ str(self.cod_album) +' '+ self.nombre +' '+ str(self.id_interprete) +' '+ str(self.id_genero) +' '+ str(self.cant_temas) +' '+ str(self.id_discografica) +' '+ str(self.id_formato) +' '+ self.fec_lanzamiento +' '+ str(self.precio) +' '+ str(self.cantidad) +' '+ self.caratula

    

    #---------------------------------------------------------------------------------------------------------

AComoAmor = Album(0,456783,'A Como Amor',3,5,10,5,3,'1978-01-01',899.99,3,'')

#con = Conectar()
#con.InsertarAlbum(AComoAmor)
