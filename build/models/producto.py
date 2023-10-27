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

    #Methods
    def crearProducto(id,nombre,marca,precio,ciudad):
        producto = Producto(id,nombre,marca,precio,ciudad)
        con =Conectar()
        con.registrarProducto(producto)