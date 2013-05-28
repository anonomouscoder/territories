class tile:
   coordinate = (0,0)
   adjacencyMap = (0)
   status = (0,0,0)
   strength = 0
   def getCoordinate(self):
      return self.coordinate
   def setCoordinate(self,coor):
      self.coordinate = coor
      
   def getAdjacencyMap(self):
      return self.adjacencyMap
   def setAdjacencyMap(self,map):
      self.adjacencyMap = map
   
   def getStatus(self):
      return self.status
   def setStatus(self,stat):
      self.status = stat
   
   def getStrength(self):
      return self.strength
   def setStrength(self,str):
      self.strength = str
      
   def __init__(self,coor,map,stat,str):
      self.setCoordinate(coor)
      self.setAdjacencyMap(map)
      self.setStatus(stat)
      self.setStrength(str)