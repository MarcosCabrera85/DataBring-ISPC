import mysql.connector

class Connect:
    def __init__(self, host='localhost', port=3306, user='root', password='', db='productos') -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = host,
                port = port,
                user = user,
                password = password,
                db = db
            )
        except mysql.connector.Error as descripcionError:
            print("NO SE PUDO CONECTAR ", descripcionError)
