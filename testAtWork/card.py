import pygame.sprite
class Card(pygame.sprite.Sprite):
   coordinate = (0,0)
   height = 200
   width = 100
   imageName = ""
   toolTip = ""
   def getCoordinate(self):
      return self.coordinate
   def setCoordinate(self,coor):
      self.coordinate = coor
      
   def getImageName(self):
      return self.imageName
   def setImageName(self,name):
      self.imageName = name
   
   def getToolTip(self):
      return self.toolTip
   def setToolTip(self,tip):
      self.toolTip = tip
         
   def __init__(self,coor,name,tip):
      pygame.sprite.Sprite.__init__(self)
      self.setCoordinate(coor)
      self.setImageName(name)
      self.setToolTip(tip)
      self.image = pygame.Surface([self.width,self.height])
      self.image.fill((0,0,0))
      self.rect = self.image.get_rect()