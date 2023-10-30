#importamos las librerias necesarias para programar la ventana
from tkinter import *
from tkinter import ttk #submodulo para crear las tablas, combobox y otras cosas

#creamos la ventana
ventana = Tk()

ventana.geometry('1000x382')

ventana.title('Registro de personas')

ventana.configure(background='burlywood1')

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

pesoLbl =Label(text='Peso:',font=('calibi',12,'bold'),bg='tan1')
pesoLbl.place(x=50,y=150)

ciudadLbl =Label(text='Ciudad:',font=('calibi',12,'bold'),bg='tan1')
ciudadLbl.place(x=50,y=200)

canastaLbl =Label(text='Canasta',font=('calibi',12,'bold'),bg='tan1')
canastaLbl.place(x=50,y=250)

#creamos las cajas de texto
nombreTxt = Entry()
nombreTxt.place(x=150,y=44, width=300, height=30)

apellidoTxt = Entry()
apellidoTxt.place(x=150,y=97, width=300, height=30)

dniTxt = Entry()
dniTxt.place(x=150,y=150, width=300, height=30)

#creamos el comboBox de ciudades
ciudadCbox = ttk.Combobox()
ciudadCbox.place(x=150,y=200,width=300,height=30)
#para no poder modificar el combobox
ciudadCbox.configure(state='readonly')

ciudad = ['Cordoba','Misiones','Salta','Santa fe','San Juan']
ciudadCbox.set(ciudad[0]) #le damos al combobox la lista y que muestre por defecto el elemento 0
ciudadCbox.configure(values=ciudad) #asi le asigno todos los datos de la lista


###Creamos los radioButtons####

control = IntVar() #variable de control
control.set(1)

siRbt = Radiobutton(text='Si',value=1,variable=control,font=('calibi',12,'bold'),bg='tan1',activebackground='tan1')
siRbt.place(x=162,y=250)

noRbt = Radiobutton(text='No',value=2,variable=control,font=('calibi',12,'bold'),bg='tan1',activebackground='tan1')
noRbt.place(x=285,y=250)

otroRbt = Radiobutton(text='Otro',value=3,variable=control,font=('calibi',12,'bold'),bg='tan1',activebackground='tan1')
otroRbt.place(x=400,y=250)

####CREAMOS LA TABLA######

columnas = ('#1','#2','#3','#4') #siempre se define con una tupla la cantidad de columnas a tener

tabla = ttk.Treeview(columns=columnas, show='headings')#asignamos las columnas de la tupla


#Una vez creada la tabla creamos los encabezados
tabla.heading('#1',text='ID') #en la tabla el heading en la col nro 1 es el texto id
tabla.heading('#2',text='Nombre')
tabla.heading('#3',text='Marca')
tabla.heading('#4',text='Peso')


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

aceptarBtn = Button(text='Aceptar',bg='tan1',font=('calibi',12,'bold'))
aceptarBtn.place(x=20,y=320,width=140,height=30)
cancelarBtn = Button(text='Cancelar',bg='tan1',font=('calibi',12,'bold'))
cancelarBtn.place(x=190,y=320,width=140,height=30)

eliminarBtn = Button(text='Eliminar',bg='tan1',font=('calibi',12,'bold'))
eliminarBtn.place(x=360,y=320,width=140,height=30)

ventana.resizable(False,False)
ventana.mainloop()