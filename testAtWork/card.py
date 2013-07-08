import pygame.sprite, drawUtils
from drawUtils import *
CLUB = 1
DIAMOND = 2
HEART = 3
SPADE = 4

JACK = 11
QUEEN = 12
KING = 13
ACE = 1

class Card(pygame.sprite.DirtySprite):
   suit = CLUB
   rank = 2
   rankImageName = ""
   suitImageName = ""
   cardImageName = ""
   toolTip = ""
   
   def getCardValue(self):
      return (self.suit,self.rank)
   def setCardValue(self, suit, rank):
      self.suit = suit
      self.rank = rank
      
   def getRankImageName(self):
      return self.rankImageName
   def getSuitImageName(self):
      return self.suitImageName
   def getCardImageName(self):
      return self.cardImageName
   def calculateImageNames(self):
      self.rankImageName = str(self.rank)
      if self.rank == JACK:
         self.rankImageName = "j.png"
      elif self.rank == QUEEN:
         self.rankImageName = "q.png"
      elif self.rank == KING:
         self.rankImageName = "k.png"
      elif self.rank == ACE:
         self.rankImageName = "a.png"
      else:
         self.rankImageName = str(self.rank)
         self.rankImageName = self.rankImageName + ".png"
      
      if self.suit == CLUB:
         self.suitImageName = "club.png"
      elif self.suit == DIAMOND:
         self.suitImageName = "diamond.png"
      elif self.suit == HEART:
         self.suitImageName = "heart.png"
      elif self.suit == SPADE:
         self.suitImageName = "spade.png"
      
      (x,y,w,h) = self.rect
      if h == 200 and w == 100:
         self.cardImageName = "100x200base.png"
   
   def getToolTip(self):
      return self.toolTip
   def setToolTip(self,tip):
      self.toolTip = tip
         
   def __init__(self,rect,suit,rank):
      pygame.sprite.Sprite.__init__(self)
      self.rect = rect
      self.setCardValue(suit,rank)
      
   def displayCard(self,groupIndex=0):
      spaceFromEdge = 3
      iconWidth = 12
      cardHeight = 200
      cardWidth = 100
      self.calculateImageNames()
      (x,y,w,h) = self.rect
      addNewSpriteToGroupByIndex("images", self.cardImageName,groupIndex,(x,y))
      addNewSpriteToGroupByIndex("images",self.rankImageName,groupIndex,(x + spaceFromEdge,            y + spaceFromEdge))
      addNewSpriteToGroupByIndex("images",self.suitImageName,groupIndex,(x + spaceFromEdge + iconWidth,y + spaceFromEdge))
      addNewSpriteToGroupByIndex("images",self.rankImageName,groupIndex,(x + cardWidth - spaceFromEdge - iconWidth,     y + cardHeight - spaceFromEdge - iconWidth))
      addNewSpriteToGroupByIndex("images",self.suitImageName,groupIndex,(x + cardWidth - spaceFromEdge - iconWidth * 2, y + cardHeight - spaceFromEdge - iconWidth))
#
# C = Card((0,0,100,200),HEART,2)
# C.displayCard()
# D = Card((27,0,100,200),SPADE,3)
# D.displayCard()
# E = Card((54,0,100,200),CLUB,4)
# E.displayCard()

# drawAllGroups()
# time.sleep(5)
