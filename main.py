from pymongo import MongoClient
import datetime
import onceStarted as oSed


#conexion con local
client = MongoClient('mongodb://localhost:27017/')

#generamos un log de acceso
rlog = oSed.log("local",client)
#comprobamos que este bien
print(rlog.checkID)

#acceso a la base de datos
#db = client.rrhh
for i in rlog.checkLogs():
	aux = i.split(',')
	print("El "+aux[0]+" ocurrio un error inesperado por: "+aux[1])

rlog.closeLogs()



#info = db.informacion






