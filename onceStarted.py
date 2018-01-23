import datetime
import sys
import getpass



class log():

	registro = datetime.datetime.utcnow()
	crhlog = None

	def __init__(self, access, cliente):
		self.crhlog = cliente.rrhh.logs
		self.access = access
		post = {'date':self.registro,'author':getpass.getpass(),'access':access,'vpython':sys.version.split()[0]}
		self.checkID = self.crhlog.insert_one(post).inserted_id

	def checkLogs(self):
		errorList = list()
		cursor = self.crhlog.find({'finished':{'$exists':False}})
		for i in cursor:
			errorList.append(str(i['date']) + ", unclosed")
		return errorList



	def closeLogs(self):
		self.crhlog.update_one({'date':self.registro},{"$set":{'finished':True}},upsert=False)


#en caso de error devovler tipo de error
#devolver numero de logs, id log y ultima conxion
#actualizar log
#buscar logs que no tengan el atributo cerrado o que si lo tenga, su valor sea True
#devolver informe y warning de errores de log



