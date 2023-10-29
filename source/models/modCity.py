class City:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre


    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre

    def setId(self,id):
        self.id = id
    def setNombre(self,nombre):
        self.nombre = nombre

    def __str__(self) -> str:
        return "ID: " + str(self.id) + "\n" + "Nombre: " + self.nombre + "\n"
