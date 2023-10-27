class Persona:
    def __init__(self,id,nombre,telefono,celular,direccion,email,foto,estado):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.celular = celular
        self.direccion = direccion
        self.email = email
        self.foto = foto
        self.estado = estado

    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getTelefono(self):
        return self.telefono
    def getCelular(self):
        return self.celular
    def getDireccion(self):
        return self.direccion
    def getEmail(self):
        return self.email
    def getFoto(self):
        return self.foto
    def getEstado(self):
        return self.estado
    
    def setId(self,id):
        self.id = id
    def setNombre(self,nombre):
        self.nombre = nombre
    def setTelefono(self,telefono):
        self.telefono = telefono
    def setCelular(self,celular):
        self.celular = celular
    def setDireccion(self,direccion):
        self.direccion = direccion
    def setEmail(self,email):
        self.email = email
    def setFoto(self,foto):
        self.foto = foto
    def setEstado(self,estado):
        self.estado = estado
    
    def __str__(self) -> str:
        return "ID: "+str(self.id)+"\n"+"Nombre: "+self.nombre+"\n"+"Tel: "+self.telefono+"\n"+"Cel: "+self.celular+"\n"+"Dereccion: "+self.direccion+"\n"+"email: "+self.email
