import time, thread
from twisted.internet import reactor, protocol
import twisted.protocols.basic 

class BoardGameServer(twisted.protocols.basic.NetstringReceiver):
   """This is just about the simplest possible protocol"""
   data = 0
   def stringReceived(self, message):
      print "Server received: ", message
      if message == "test":
         self.sendString("testAck")
      elif message == "increment":
         self.data = self.data + 1
         self.sendString("incrementAck")
      elif "set" in message: #'set 1' sets data to 1
         splitMessage = message.split()
         success = False
         for word in splitMessage:
            if word.isdigit():
               self.data = int(word)
               self.sendString("setAck")
               success = True
               break
         if not success:
            self.sendString("Nack")
      elif message == "get":
         self.sendString(str(self.data))
      else:
         self.sendString("Nack")

class BoardGameClient(twisted.protocols.basic.NetstringReceiver):
   """Once connected, send a message, then print the result."""
   packetsPass = False
   messagesToPass = ["increment",
                     "increment",
                     "get",
                     "set 20",
                     "get",
                     "set a10",
                     "get"
                    ]
   index = 0
   def connectionMade(self):
      self.sendString("test")
      
   def stringReceived(self, message):
      print "Client received: ", message
      time.sleep(1)
      if message == "testAck":
         self.packetsPass = True
      if self.packetsPass == True:
         if self.index < len(self.messagesToPass):
            self.sendString(self.messagesToPass[self.index])
            self.index = self.index + 1
         else:
            self.closeConnection()
   def closeConnection(self):
      self.transport.loseConnection()
      
   def connectionLost(self, reason):
      print "connection lost"

class BoardGameClientFactory(protocol.ClientFactory):
    protocol = BoardGameClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()

class BoardGameNetworkInterface():
   #client sends tile index to attack
   #server sends True (success) or False (failure)
   clientFactory = BoardGameClientFactory()
   hostname = "localhost"
   port = 8000
   def __init():
      self.clientFactory = BoardGameClientFactory()
      hostname = "localhost"
      port = 8000
   def setHostname(self,h):
      self.hostname = h
   def setPort(self,p):
      self.port = p
   def createHost(self):
      factory = protocol.ServerFactory()
      factory.protocol = BoardGameServer
      reactor.listenTCP(self.port,factory)
   def connectToHost(self):
      reactor.connectTCP(self.hostname, self.port, self.clientFactory)
   def run(self):
      reactor.run()
def main():
   interface = BoardGameNetworkInterface()
   interface.createHost()
   interface.connectToHost()
   interface.run()
   
#   f.protocol.closeConnection()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
