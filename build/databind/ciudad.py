


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
