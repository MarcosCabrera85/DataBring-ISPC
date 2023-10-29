import mysql.connector
from models.modCity import *

class DataCity:
    def __init__(self, db) -> None:
        self.db = db
        self.cursor = db.cursor()


    def listCity(self):
        if self.db.is_connected():
            try:
                consultaSql = 'SELECT * from ciudad'
                self.cursor.execute(consultaSql)
                resultado = self.cursor.fetchall()
                self.db.close()
                return resultado
            except mysql.connector.Error as descripcionError:
                print("NO SE PUDO BUSCAR CIUDADES ", descripcionError)
