import mysql.connector
from models.modProduct import *

class DataProduct:
    def __init__(self, db) -> None:
        self.db = db
        self.cursor = db.cursor()


    def listProducts(self):
        if self.db.is_connected():
            try:
                consultaSql = 'SELECT id,nombre,marca,precio FROM productos'
                self.cursor.execute(consultaSql)
                resultado = self.cursor.fetchall() #todo lo q me trae el cursor lo meto en la lista resultado
                return resultado
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO BUSCAR PRODUCTOS ", descripcionError)
        else:
            print('NO ESTA CONECTADO')


    def registerProduct(self,producto):
        if self.db.is_connected():
            try:
                consultaSql = 'INSERT INTO productos VALUES(NULL,%s,%s,%s,%s)'
                datos = (
                    producto.getNombre(),
                    producto.getMarca(),
                    producto.getPrecio(),
                    producto.getCiudad(),
                )
                self.cursor.execute(consultaSql,datos)
                self.db.commit()
                print('PRODUCTO INSERTADO CORRECTAMENTE!')
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO REGISTRAR ", descripcionError)
        else:
            print('NO ESTA CONECTADO')


    def deleteProduct(self,id):
        if self.db.is_connected():
            try:
                consultaSql = 'DELETE from productos WHERE id = %s'
                datos = (id,)
                self.cursor.execute(consultaSql,datos)
                self.db.commit()
                print('PRODUCTO ELIMINADO CORRECTAMENTE')
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO ELIMINAR ", descripcionError)
        else:
            print('NO ESTA CONECTADO')

    def updateProduct(self,producto):
        if self.db.is_connected():
            try:
                consultaSql = 'UPDATE productos SET nombre =%d, marca =%d, precio =%d, ciudad=%d WHERE id = %d'
                datos = (
                    producto.getNombre(),
                    producto.getMarca(),
                    producto.getPrecio(),
                    producto.getCiudad()
                )
                self.cursor.execute(consultaSql,datos)
                self.db.commit()
                print("Producto Actualizado correctamente!")
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO ACTUALIZAR ", descripcionError)
        else:
            print('NO ESTA CONECTADO')


    def createProduct(self, id, nombre, marca, precio, ciudad):
        producto = Product(id, nombre, marca, precio, ciudad)
        self.registerProduct(producto)
