
import mysql.connector

class Producto:
    #1ro el constructor
    def __init__(self,id,nombre,marca,precio,ciudad) -> None:
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.ciudad = ciudad
    
    #metodo toString()

    def __str__(self) -> str:
        return str(self.id) +' '+ self.nombre +' '+ self.marca +' '+ self.precio +' '+ self.ciudad
    
    #getter

    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getMarca(self):
        return self.marca
    def getPrecio(self):
        return self.precio
    def getCiudad(self):
        return self.ciudad
    
    #Setters
    def setId(self,id):
        self.id = id
    def setId(self,nombre):
        self.nombre = nombre
    def setId(self,marca):
        self.marca = marca
    def setId(self,precio):
        self.precio = precio
    def setId(self,ciudad):
        self.ciudad = ciudad

#clase conexion a la BD

class Conectar:
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'productos'
            )
        except mysql.connector.Error as descripcionError:
            print("NO SE PUDO CONECTAR ", descripcionError)

    def listarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = 'SELECT id,nombre,marca,precio FROM productos'
                cursor.execute(consultaSql)
                resultado = cursor.fetchall() #todo lo q me trae el cursor lo meto en la lista resultado
                self.conexion.close()
                return resultado
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO CONECTAR ", descripcionError)

    def listarCiudad(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = 'SELECT * from ciudad'
                cursor.execute(consultaSql)
                resultado = cursor.fetchall()
                self.conexion.close()
                return resultado
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO CONECTAR ", descripcionError)


    def registrarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = 'INSERT INTO productos VALUES(NULL,%s,%s,%s,%s)'
                datos = (
                    producto.getNombre(),
                    producto.getMarca(),
                    producto.getPrecio(),
                    producto.getCiudad()
                )
                cursor.execute(consultaSql,datos)
                self.conexion.commit()
                self.conexion.close()
                print('PRODUCTO INSERTADO CORRECTAMENTE!')
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO CONECTAR ", descripcionError)
    
    def eliminarProducto(self,id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = 'DELETE from productos WHERE id = %s'
                datos = (id,)
                cursor.execute(consultaSql,datos)
                self.conexion.commit()
                self.conexion.close()
                print('PRODUCTO ELIMINADO CORRECTAMENTE')
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO CONECTAR ", descripcionError)

    def actualizarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = 'UPDATE productos SET nombre =%d, marca =%d, precio =%d, ciudad=%d WHERE id = %d'
                datos = (
                    producto.getNombre(),
                    producto.getMarca(),
                    producto.getPrecio(),
                    producto.getCiudad()
                )
                cursor.execute(consultaSql,datos)
                self.conexion.commit()
                self.conexion.close()
                print("Producto Actualizado correctamente!")
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO CONECTAR ", descripcionError)

#necesito una funcion para crear un objeto de tipo producto para que con los datos de la ventana mande a la bd

def crearProducto(id,nombre,marca,precio,ciudad):
    producto = Producto(id,nombre,marca,precio,ciudad)
    con =Conectar()
    con.registrarProducto(producto)
