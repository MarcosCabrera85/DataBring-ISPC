#aca vamos a incluir todas las funciones con  las cual vamos a trabajar
#tareas de acceso a la bd, listado, borrado
#esta funcionalidad va a hacer uso de las clases del modulo modelo.py

'''
funcionalidades:
def listarContactos()
def crearContacto()
def editarContacto()
def eliminarContacto()

'''

import modelo

def listarContactos(): #me va a traer desde la bd todos los contactos q tenga
    con = modelo.Conectar() #con es la instancia de la Clase conectar que está en modelo
    listado = con.listarPersonas() #como ahora con es un objeto conectar puede utilizar todos sus metodos

    for contacto in listado:
        print("Nombre: "+contacto[1]+" Teléfono: "+contacto[2]+" Celular: "+contacto[3]+" Dirección: "+contacto[4]+" Email: "+contacto[5])
    
    input("\n Presione Enter para continuar >>>")
#-----------------------------------------------------------------------------------------------------------------
def crearContacto():
    nombre = input("Ingrese el nombre completo del Nvo contacto: ") #como el contacto es nvo tengo q pedirle q lo agregue
    telefono = input("Ingrese el teléfono: ")
    celular = input("Ingrese el celular: ")
    direccion = input("Ingrese la direccion: ")
    email = input("Ingrese el email: ")
    foto = ""
    

    ctoNuevo = modelo.Persona(0,nombre,telefono,celular,direccion,email,foto)
    
    con = modelo.Conectar()
    con.insertarPersona(ctoNuevo)

    input("\n Presione Enter para continuar >>>")
#-----------------------------------------------------------------------------------------------------------------
def editarContacto(): #el usuario necesita ver cuales son las opciones para poder editar
    con = modelo.Conectar()
    listado = con.listarPersonas()

    for contacto in listado:
        print("ID: "+str(contacto[0])+"| Nombre: "+contacto[1]+" Teléfono: "+contacto[2]+" Celular: "+contacto[3]+" Dirección: "+contacto[4]+" Email: "+contacto[5])
    
    id = int(input("\n Ingrese el Id del contacto que quiere EDITAR: "))

    con = modelo.Conectar()
    contacto = con.buscarPersona(id)

    if contacto == None: #Si el contacto no tiene nada imprimimos un mje:
        print("\n La busqueda no arrojó resultados")
    else:
        print("Nombre: "+contacto[1]+" Teléfono: "+contacto[2]+" Celular: "+contacto[3]+" Dirección: "+contacto[4]+" Email: "+contacto[5])
        nombre = input("\nIngrese el nvo nombre o ENTER para omitir: ")
        if nombre == "":
            nombre = contacto[1]
        
        telefono = input("\nIngrese el nvo Telefono o ENTER para omitir: ")
        if telefono == "":
            telefono = contacto[2]

        celular = input("\nIngrese el nvo celular o ENTER para omitir: ")
        if celular == "":
            celular = contacto[3]

        direccion = input("\nIngrese la nva dirección o ENTER para omitir: ")
        if direccion == "":
            direccion = contacto[4]
        
        email = input("\nIngrese el nvo email o ENTER para omitir: ")
        if email == "":
            email = contacto[5]
        
        contactoEditado = modelo.Persona(id,nombre,telefono,celular,direccion,email,None,1)

        conEdit = modelo.Conectar()
        conEdit.modificarPersona(contactoEditado)

    input("\n Presione Enter para continuar >>>")
#-------------------------------------------------------------------------------------------------------------
def eliminarContacto():
    con = modelo.Conectar()
    listado = con.listarPersonas()

    for contacto in listado:
        print("ID: "+str(contacto[0])+"Nombre: "+contacto[1]+" Teléfono: "+contacto[2]+" Celular: "+contacto[3]+" Dirección: "+contacto[4]+" Email: "+contacto[5])
    
    id = int(input("\n Ingrese el Id del contacto que quiere ELIMINAR: "))

    con = modelo.Conectar() #Lo creamos de nvo simplemente porq cuando se conecta a la base de datos antes, tre el listado y cierra la conexion... entonces hay q crear una instancia nueva de Conectar
    contacto = modelo.Persona(id,"","","","","","",1)

    con.eliminarPersona(contacto)

    input("\n Presione Enter para continuar >>>")








listarContactos()
