# Para este proyecto, buscamos extraer los datos de los productos y del precio del mismo de la pagina web de Hiper Libertad:
# https://www.hiperlibertad.com.ar/

# 01 - Importamos las librerias necesarias:
import scrapy
from datetime import datetime

# 02-  Configuramos la fecha  y hora actual:
hora = datetime.now().time()
fecha = datetime.now().today()