from socket import *

class Server:
	hostName=''
	hostPort=0
	serverSocket=None
	connection=None
	addr=''
	
	def __init__(self,name,port):
		self.hostName=name
		self.hostPort=port
		self.serverSocket=socket()
		self.serverSocket.bind((self.hostName,self.hostPort))
		self.serverSocket.listen(5)
		
	def serverMessage(self,message):
		print "%s\n" % (message)
		
	def connectClient(self):
		self.connection,self.addr=self.serverSocket.accept()		
		msg="Connected to: "+str(self.addr)
		self.serverMessage(msg)
			
	def messageToClient(self,message):
		msg="Server: "+message+" \n"		
		self.connection.send(msg)
		
	def receiveDataFromClient(self,buffer):
		data=self.connection.recv(buffer)
		return data
		
	def fileOperation(self,filename,text):
		fp=open(filename,"w")
		fp.write(text)
		fp.close()		
		
	def closeConnection(self):
		self.messageToClient("Closing Connection!\n")
		self.connection.close()		
		self.serverMessage("Closing server!\n")
		self.serverSocket.close()
		
#main
if __name__=="__main__":
	serverObj=Server('',51233)
	while True:
		serverObj.connectClient()		
		serverObj.messageToClient("Enter the filename: ")		
		filename=serverObj.receiveDataFromClient(256)
		serverObj.serverMessage("Got filename\n")
		serverObj.messageToClient("Got filename\n")
		
		text=serverObj.receiveDataFromClient(2048)
		serverObj.serverMessage("Got file data\n")
		serverObj.messageToClient("Got file data\n")
		
		serverObj.serverMessage("Writing file\n")
		serverObj.messageToClient("Writing file\n")
		newname="/home/virus/Desktop/"+filename
		serverObj.fileOperation(newname,text)
		
		serverObj.serverMessage("Done\n")
		serverObj.messageToClient("Done\n")
		
		serverObj.closeConnection()
		
		break
		
		
	
	
	
		
	
		
		
		
		
