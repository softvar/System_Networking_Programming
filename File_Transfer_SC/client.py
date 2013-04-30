from socket import *

class Client:
	hostName=""
	hostPort=0
	clientSocket=None
	
	def __init__(self,name,port):
		self.hostName=name
		self.hostPort=port
		self.clientSocket=socket()
		self.clientSocket.connect((self.hostName,self.hostPort))
		
	def receiveDataFromServer(self):
		data=self.clientSocket.recv(1024)
		return data
		
	def getDataFromUser(self,message):
		data=raw_input(message)
		return data
		
	def sendDataToServer(self,data):
		self.clientSocket.send(data)
		
	def closeConnection(self):
		clientSocket.close()
		
	def clientMessage(self,message):
		print "%s" % (message)
		
	def fileOperation(self,filename):
		text=''
		fp=open(filename,"r")
		for line in fp.readlines():
			text=text+line
		return text
		
if __name__=="__main__":
	clientObj=Client("localhost",51233)
	
	#getting filename from user and sending file to server
	data=clientObj.receiveDataFromServer()	
	filename=clientObj.getDataFromUser(data)
	clientObj.sendDataToServer(filename)	
	data=clientObj.receiveDataFromServer()	
	clientObj.clientMessage(data)
	
	#getting file data and sending to server
	text=clientObj.fileOperation(filename)
	clientObj.sendDataToServer(text)
	data=clientObj.receiveDataFromServer()	
	clientObj.clientMessage(data)
	
	data=clientObj.receiveDataFromServer()	
	clientObj.clientMessage(data)	
