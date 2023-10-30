from databind.dbCity import *
from databind.dbProduct import *
from tkinter import *
from tkinter import ttk #submodulo para crear las tablas, combobox y otras cosas

class ViewProduct:
    def __init__(self, db):
        self.db = db
        self.dataProduct = DataProduct(db)
        self.dataCity = DataCity(db)


    ##creamos una funcion que vamos a invocar cuando creemos el boton listar, para insertar los datos en la tabla de la ventana###
    def viewListProducts(self, tabla):
        datos =[]  #aca guardamos los datos de la bd
        productos = self.dataProduct.listProducts()
        if productos != None:
            self.viewEmptyTable(tabla)
            #recorremos la lista q devuelve el metodo listarProductos en la clase conectar
            for producto in productos:
                datos.append(producto)
            #ahora metemos los datos a la tabla.. recorremos los datos q estan en la lista datos q declare vacia y ahora esta con los objetos de la tabla
            for dato in datos:
                tabla.insert('',END,values=dato)
            ###-->'' hace referencia a q lugar de la tabla
            ###-->END para q vaya agregando secuencialmente y no pise datos de la tabla
            ###-->values = dato cada dato q hay en la lista dato lo tome como un valor para la tabla
        else:
            print('Nohay productos para listar')


    #creamos una funcion para insertar un producto
    def viewCreateProduct(self, tabla, producto, marca, precio, city):
        self.dataProduct.createProduct(0, producto.get(), marca.get(), precio.get(), city.get())
        self.viewListProducts(tabla) #para q me refresque la tabla con los productos


    #Funcion para el boton limpiar datos
    def viewEmptyTable(self, tabla):
        for fila in tabla.get_children(): #los niños es un metodo que hace referencia a unas dependencias.. y no se que mas pero asi se limpia
            tabla.delete(fila)
        self.view.update()


    def viewEmptyFields(self, tabla, producto, marca, precio):
        self.viewEmptyTable(tabla)
        producto.delete(0,'end') #que borre de principio a fin dentro del campo
        marca.delete(0,'end')
        precio.delete(0,'end')


    #funcion para borrar producto
    def viewDeleteProduct(self, tabla):
        seleccion = tabla.focus()
        if seleccion != "":
            id = tabla.item(seleccion)['values'][0]
            self.dataProduct.deleteProduct(id)
        self.viewEmptyTable(tabla)
        self.viewListProducts(tabla)


    def viewCityNames(self):
        localidades = self.dataCity.listCity()
        nombres = []
        if localidades != None:
            #recorremos la lista de ciudades de la base de datos
            for localidad in localidades:
                nombres.append(localidad[1])
        return nombres


    #####                    #####
    ##### Creamos la ventana #####
    #####                    #####

    def initView(self):
        view = Tk()
        view.geometry('1000x382')
        view.title('Registro de Productos')
        view.configure(background='burlywood1')
        self.view = view

        #creamos el marco de ingreso de datos
        marco = LabelFrame()
        marco.place(x=20,y=20, width=480, height=280)
        marco.configure(background='tan1')

        #creamos las etiquetas
        productoLbl = Label(text='Producto:', font=('calibi',12,'bold'),bg='tan1')
        #damos la ubicacion de la etiqueta
        productoLbl.place(x=50,y=50)
        marcaLbl =Label(text='Marca:',font=('calibi',12,'bold'),bg='tan1')
        marcaLbl.place(x=50, y=100)
        precioLbl =Label(text='Precio:',font=('calibi',12,'bold'),bg='tan1')
        precioLbl.place(x=50,y=150)
        ciudadLbl =Label(text='Ciudad:',font=('calibi',12,'bold'),bg='tan1')
        ciudadLbl.place(x=50,y=200)
        #canastaLbl =Label(text='Canasta',font=('calibi',12,'bold'),bg='tan1')
        #canastaLbl.place(x=50,y=250)

        #creamos las cajas de texto
        productoTxt = Entry()
        productoTxt.place(x=150,y=44, width=300, height=30)
        marcaTxt = Entry()
        marcaTxt.place(x=150,y=97, width=300, height=30)
        precioTxt = Entry()
        precioTxt.place(x=150,y=150, width=300, height=30)

        #-----------------------------------------------------------------------------------------------------------
        #vamos a cargar el combo de las ciudades desde la base de datos...
        ciudad = self.viewCityNames()
        #-----------------------------------------------------------------------------------------------------------
        #creamos el comboBox de ciudades
        ciudadCbox = ttk.Combobox()
        ciudadCbox.place(x=150,y=200,width=300,height=30)
        #para no poder modificar el combobox
        ciudadCbox.configure(state='readonly')
        #ciudad = ['Cordoba','Misiones','Salta','Santa fe','San Juan','Tucuman']
        if ciudad != []:
            ciudadCbox.set(ciudad[0]) #le damos al combobox la lista y que muestre por defecto el elemento 0
        ciudadCbox.configure(values=ciudad) #asi le asigno todos los datos de la lista

        ###Creamos los radioButtons####
        #control = IntVar() #variable de control
        #control.set(1)
        #siRbt = Radiobutton(text='Si',value=1,variable=control,font=('calibi',12,'bold'),bg='tan1',activebackground='tan1')
        #siRbt.place(x=162,y=250)
        #noRbt = Radiobutton(text='No',value=2,variable=control,font=('calibi',12,'bold'),bg='tan1',activebackground='tan1')
        #noRbt.place(x=285,y=250)
        #otroRbt = Radiobutton(text='Otro',value=3,variable=control,font=('calibi',12,'bold'),bg='tan1',activebackground='tan1')
        #otroRbt.place(x=400,y=250)

        ####CREAMOS LA TABLA######
        columnas = ('#1','#2','#3','#4') #siempre se define con una tupla la cantidad de columnas a tener
        tabla = ttk.Treeview(columns=columnas, show='headings')#asignamos las columnas de la tupla
        #Una vez creada la tabla creamos los encabezados
        tabla.heading('#1',text='ID') #en la tabla el heading en la col nro 1 es el texto id
        tabla.heading('#2',text='Nombre')
        tabla.heading('#3',text='Marca')
        tabla.heading('#4',text='Precio')
        #debo darle la dimension a las columnas
        tabla.column('#1',width=115)
        tabla.column('#2',width=115)
        tabla.column('#3',width=115)
        tabla.column('#4',width=115)
        #tabla.column('#5',width=50)
        #doy color a los campos de la tabla
        estilo = ttk.Style()
        estilo.configure('Treeview',background='tan1')
        #mostramos la tabla creada
        tabla.place(x=520,y=20,width=460,height=342)

        ###CREAMOS Y PROGRAMAMOS LOS BOTONES FUNCIONALES###
        listarBtn =Button(text='Listar',bg='tan1',font=('calibi',12,'bold'),command=lambda:self.viewListProducts(tabla))
        listarBtn.place(x=50,y=250, width=84, height=30)
        limpiarBtn = Button(text='Limpiar',bg='tan1',font=('calibi',12,'bold'),command=lambda:self.viewEmptyFields(tabla, productoTxt, marcaTxt, precioTxt))
        limpiarBtn.place(x=162,y=250, width=84, height=30)
        aceptarBtn = Button(text='Aceptar',bg='tan1',font=('calibi',12,'bold'),command=lambda:self.viewCreateProduct(tabla, productoTxt, marcaTxt, precioTxt, ciudadCbox))
        aceptarBtn.place(x=20,y=320,width=140,height=30)
        cancelarBtn = Button(text='Cancelar',bg='tan1',font=('calibi',12,'bold'),command=lambda:self.viewEmptyFields(tabla, productoTxt, marcaTxt, precioTxt))
        cancelarBtn.place(x=190,y=320,width=140,height=30)
        eliminarBtn = Button(text='Eliminar',bg='tan1',font=('calibi',12,'bold'),command=lambda:self.viewDeleteProduct(tabla))
        eliminarBtn.place(x=360,y=320,width=140,height=30)

        view.resizable(False,False)
        view.mainloop()
