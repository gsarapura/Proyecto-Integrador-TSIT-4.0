# Acomodar los métodos Listar
# Colocar if self.conexion.is_connected(): dentro de try - except?
# Por qué comentar los #self.conexion.close():?
# Métodos insertar # Vengan como objeto?
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
# Como está.    
    def ListarAlbumes(self):
        if self.conexion.is_connected(): # Duda
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT cod_album, nombre_album, nombre_interprete, apellido_apellido, nombre_gen, nombre_disc, precio, cantidad, formato.tipo FROM album, interprete, discografica,formato,genero WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero ORDER By interprete.apellido desc"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!",descripcionError) # Duda poner el error afuera?

    def ListarPorGenero(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT cod_album, album.nombre, interprete.nombre, interprete.apellido, genero.nombre, discografica.nombre, precio, cantidad, formato.tipo FROM album, interprete, discografica,formato,genero WHERE album.id_interprete = interprete.id_interprete AND album.id_discografica = discografica.id_discografica AND album.id_formato = formato.id_formato AND album.id_genero = genero.id_genero ORDER By genero.nombre asc"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                 # why dis
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

    
    def ModificarAlbum(self,album):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE album SET nombre = %s, id_interprete = %s, id_genero = %s, cant_temas = %s, id_discografica = %s, id_formato = %s, fec_lanzamiento = %s, precio = %s, cantidad = %s, caratula = %s WHERE cod_album = %s"

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
                print("Álbum modificado correctamente")

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

    def __init__(self, id_interprete, nombre_interprete, apellido_interprete, nacionalidad, foto) -> None:
        self.id_interprete = id_interprete
        self.nombre_interprete = nombre_interprete
        self.apellido_interprete = apellido_interprete
        self.nacionalidad = nacionalidad
        self.foto = foto

    def getId_interprete(self):
        return self.id_interprete
    def getNombre_int(self):
        return self.nombre_interprete
    def getApellido_int(self):
        return self.apellido_interprete
    def getNacionalidad(self):
        return self.nacionalidad
    def getFoto(self):
        return self.foto

    def setId_interprete(self,idInterprete):
        self.id_interprete = idInterprete
    def setNombre_int(self,nombre_interprete):
        self.nombre_interprete = nombre_interprete
    def setApellido_int(self,apellido_interprete):
        self.apellido_interprete = apellido_interprete
    def setNacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad
    def setFoto(self,foto):
        self.foto = foto

    def __str__(self) -> str:
        return str(self.id_interprete)+' '+self.nombre_interprete+' '+self.apellido_interprete+' '+self.nacionalidad+' '+self.foto

#---------------------------------------------------------------------------------------

class Genero():
    def __init__(self,id_genero,nombre_gen) -> None:
        self.id_genero = id_genero
        self.nombre_gen = nombre_gen

    def __str__(self) -> str:
        return str(self.id_genero)+' '+self.nombre_gen

    def getId_genero(self):
        return self.getId_genero
    def getNombre_gen(self):
        return self.nombre_gen

    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setNombre_gen(self,nombre_gen):
        self.nombre_gen = nombre_gen


#---------------------------------------------------------------------------------------

class Discografica():
    def __init__(self,id_discografica,nombre_disc) -> None:
        self.id_discografica = id_discografica
        self.nombre_disc = nombre_disc

    def __str__(self) -> str:
        return str(self.id_discografica)+' '+self.nombre_disc

    def getId_discografica(self):
        return self.id_discografica
    def getNombre_disc(self):
        return self.nombre_disc
    
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setNombre_disc(self,nombre_disc):
        self.nombre_disc = nombre_disc


#---------------------------------------------------------------------------------------

class Formato():
    def __init__(self,id_formato,tipo_formato) -> None:
        self.id_formato = id_formato
        self.tipo_formato = tipo_formato

    def __str__(self) -> str:
        return str(self.id_formato)+' '+self.tipo_formato

    def getId_formato(self):
        return self.id_formato
    def getTipo_formato(self):
        return self.tipo_formato

    def setId_formato(self,id_formato):
        self.id_formato = id_formato
    def setTipo_formato(self,tipo_formato):
        self.tipo_formato = tipo_formato

#---------------------------------------------------------------------------------------


class Tema():
    def __init__(self, id_tema, nombre_tema, autor, compositor) -> None:
        self.id_tema = id_tema
        self.nombre_tema = nombre_tema
        self.autor = autor
        self.compositor = compositor

    def getId_tema(self):
        return self.id_tema

    def getNombre_tema(self):
        return self.nombre_tema

    def getAutor(self):
        return self.autor

    def getCompositor(self):
        return self.compositor

    def setId_tema(self, id_tema):
        self.id_tema = id_tema

    def setNombre_tema(self, nombre_tema):
        self.nombre_tema = nombre_tema

    def setAutor(self, autor):
        self.autor = autor

    def setCompositor(self, compositor):
        self.compositor = compositor

    def __str__(self) -> str:
        return str(self.id_tema)+' '+self.nombre_tema+' '+self.autor+' '+self.compositor

#---------------------------------------------------------------------------------------


class Album_Tema():
    def __init__(self, cod_album, id_tema) -> None:
        self.cod_album = cod_album
        self.id_tema = id_tema

    def getId_tema(self):
        return self.id_tema

    def getCod_album(self):
        return self.cod_album

    def setId_tema(self, id_tema):
        self.id_tema = id_tema

    def setCod_album(self, cod_album):
        self.cod_album = cod_album

    def __str__(self) -> str:
        return str(self.id_tema)+' '+str(self.cod_album)

#---------------------------------------------------------------------------------------


class Interprete_Tema():
    def __init__(self, duracion, id_interprete, id_tema) -> None:
        self.duracion = duracion
        self.id_interprete = id_interprete
        self.id_tema = id_tema

    def getId_tema(self):
        return self.id_tema

    def getDuracion(self):
        return self.duracion

    def getId_interprete(self):
        return self.id_interprete

    def setId_tema(self, id_tema):
        self.id_tema = id_tema

    def setDuracion(self, duracion):
        self.duracion = duracion

    def setId_interprete(self, id_interprete):
        self.id_interprete = id_interprete

    def __str__(self) -> str:
        return str(self.id_tema)+' '+str(self.duracion)+' '+str(self.id_interprete)



#---------------------------------------------------------------------------------------

class Album():
    def __init__(self,cod_album,nombre_album,id_genero,cant_temas,id_discografica,fec_lanzamiento,precio,cantidad,caratula) -> None:
        self.cod_album = cod_album
        self.nombre_album = nombre_album
        self.id_genero = id_genero
        self.cant_temas = cant_temas
        self.id_discografica = id_discografica
        self.fec_lanzamiento = fec_lanzamiento
        self.precio = precio
        self.cantidad = cantidad
        self.caratula = caratula

    def getCod_album(self):
        return self.cod_album
    def getNombre(self):
        return self.nombre_album
    def getId_genero(self):
        return self.id_genero
    def getCant_temas(self):
        return self.cant_temas
    def getId_discografica(self):
        return self.id_discografica
    def getFec_lanzamiento(self):
        return self.fec_lanzamiento
    def getPrecio(self):
        return self.precio
    def getCantidad(self):
        return self.cantidad
    def getCaratula(self):
        return self.caratula

    def setCod_album(self,cod_album):
        self.cod_album = cod_album
    def setNombre_album(self,nombre_album):
        self.nombre_album = nombre_album
    def setId_genero(self,id_genero):
        self.id_genero = id_genero
    def setCant_temas(self,cant_temas):
        self.cant_temas = cant_temas
    def setId_discografica(self,id_discografica):
        self.id_discografica = id_discografica
    def setFec_lanzamiento(self,fec_lanzamiento):
        self.fec_lanzamiento = fec_lanzamiento
    def setPrecio(self,precio):
        self.precio = precio
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    def setCaratula(self,caratula):
        self.caratula = caratula

    def __str__(self) -> str:
        return str(self.cod_album) + ' ' + self.nombre_album + ' ' + str(self.id_genero) + ' ' + str(self.cant_temas) + ' ' + str(self.id_discografica) + ' ' + self.fec_lanzamiento + ' ' + str(self.precio) + ' ' + str(self.cantidad) + ' ' + self.caratula

    #---------------------------------------------------------------------------------------


class Album_Formato():
    def __init__(self, id_formato, cod_album) -> None:
        self.cod_album = cod_album
        self.id_formato = id_formato

    def getId_formato(self):
        return self.id_formato

    def getCod_album(self):
        return self.cod_album

    def setId_formato(self, id_formato):
        self.id_formato = id_formato

    def setCod_album(self, cod_album):
        self.cod_album = cod_album

    def __str__(self) -> str:
        return str(self.id_formato)+' '+str(self.cod_album)
#---------------------------------------------------------------------------------------


class Album_Interprete():
    def __init__(self, cod_album, id_interprete) -> None:
        self.cod_album = cod_album
        self.id_interprete = id_interprete

    def getId_interprete(self):
        return self.id_interprete

    def getCod_album(self):
        return self.cod_album

    def setId_interprete(self, id_interprete):
        self.id_interprete = id_interprete

    def setCod_album(self, cod_album):
        self.cod_album = cod_album

    def __str__(self) -> str:
        return str(self.cod_album)+' '+str(self.id_interprete)
    #---------------------------------------------------------------------------------------------------------

#AComoAmor = Album(0,456783,'A Como Amor',3,5,10,5,3,'1978-01-01',899.99,3,'')

con = Conectar()
#con.InsertarAlbum(AComoAmor)
print(con.ListarInterprete())
