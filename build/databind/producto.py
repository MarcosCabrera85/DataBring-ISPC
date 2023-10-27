

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
