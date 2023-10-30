from models.modDatabase import *
from views.viewProducto import *

## 'ispc','Ispc*2023'  ##
db = Connect(user='ispc', password='Ispc*2023', db='libertad')
view = ViewProduct(db.conexion)
view.initView()
db.conexion.close()
