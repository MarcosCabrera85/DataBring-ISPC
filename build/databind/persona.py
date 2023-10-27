    def listarPersonas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #el cursor es el enlace con la base de datos la posicion en memoria para traer datos de la bd apunta a la tabla q le digo de la db
                consultaSql = "select * from persona"
                cursor.execute(consultaSql)
                resultados = cursor.fetchall() #fetchall es para q la info q apunta el cursor la traiga toda a python en una lista
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError: #aca ponemos q capture la excepcion mysql.connector.error le ponemos un alias y lo pasamos por el print
                print("No se pudo conectar! debido a:",descripcionError)

    def insertarPersona(self,persona): #le tenemos q mandar un objeto persona
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = "INSERT INTO persona VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)" #a los %s los despues los cambio con la info que viene por parametro de la persona, de esta forma se evita la inyeccion sql
                
                datos = (
                    persona.getNombre(),
                    persona.getTelefono(),
                    persona.getCelular(),
                    persona.getDireccion(),
                    persona.getEmail(),
                    persona.getFoto(),
                    persona.getEstado()
                ) #hacemos una tupla donde metemos todos los datos q van a ir a los %s
                

                cursor.execute(consultaSql,datos) #cuando ejecutamos la consulta le pasamos los datos con la tupla, los objetos %s se reemplazan con los de la tupla
                #como no hay nada q devolver no incluyo el resultado.fetchall()
                #tambien necesito dar un commit(es un nivel mas de seguridad de python para q se ejecute en la base de datos la modificacion)
                self.conexion.commit() #(como aca estamos cambiando cosas en la bd hace falta esto)
                self.conexion.close()
                print("Se agrego correctamente la persona")

            except mysql.connector.Error as descripcionError:
                print("No se puede conectar! debido a:",descripcionError)


    def eliminarPersona(self,persona): #La idea es que con el estado indique cual borrar nomas no borrarla directamente
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = "UPDATE persona SET estado = 0 WHERE id = %s"
                datos = (
                    persona.getId(),  #<-- como tiene un solo dato para que Python interprete q es una tupla le pongo una coma
                )
                cursor.execute(consultaSql,datos)
                self.conexion.commit()
                self.conexion.close()
                print("El contacto se ha eliminado correctamente")
            
            except mysql.connector.Error as descripcionError:
                print("No se puede conectar! debido a:",descripcionError)
    

    def modificarPersona(self,persona):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                consultaSql = "UPDATE persona SET nombre = %s,telefono = %s,celular = %s,direccion = %s,email = %s,foto = %s,estado = %s WHERE id = %s"
                datos = (
                    persona.getNombre(),
                    persona.getTelefono(),
                    persona.getCelular(),
                    persona.getDireccion(),
                    persona.getEmail(),
                    persona.getFoto(),
                    persona.getEstado(),
                    persona.getId()  #<-- esta tupla se va reemplazando del primero al ultimo %s ojo con las posiciones
                )
                cursor.execute(consultaSql,datos)
                self.conexion.commit()
                self.conexion.close()
                print("La persona se modifico correctamente")
            
            
            except mysql.connector.Error as descripcionError:
                print("No se puede conectar! debido a:",descripcionError)

    def buscarPersona(self,id):
        if self.conexion.is_connected():
            try:
                cursor =self.conexion.cursor()
                consultaSql = "SELECT * FROM persona WHERE id = %s"
                datos = (id,)

                cursor.execute(consultaSql,datos)
                resultado = cursor.fetchone()

                self.conexion.commit()
                self.conexion.close()

                return resultado
            except mysql.connector.Error as descripcionError:
                print("No se puede conectar! debido a:",descripcionError)
