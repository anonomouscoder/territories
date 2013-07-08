import pygame, sys, os, time
from pygame.locals import *
from pygame import font
from pygame.sprite import DirtySprite, LayeredDirty
pygame.init()
global allFont
allFont = font.SysFont("monospace",15)
# set up the window
global MAINWINDOW
MAINWINDOW = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Territories')
global fullWindowGroup
fullWindowGroup = LayeredDirty()
global groupList
groupList = []
groupList.append(fullWindowGroup)
def drawSquare(xposition,yposition,length,color):
   pygame.draw.rect(MAINWINDOW, color, (xposition,yposition,length,length))

#groups
def addGroup():
   newGroup = LayeredDirty()
   groupList.append(newGroup)
def drawGroup(group):
   dirty = group.draw(MAINWINDOW)
   pygame.display.update(dirty)
def drawAllGroups():
   for g in groupList:
      drawGroup(g)
#dirty dirty sprites
def addNewSpriteToGroupByIndex(directory,filename,groupIndex,(xOffset,yOffset)):
   image = pygame.image.load(os.path.join(directory,filename))
   sprite = DirtySprite()
   sprite.image = image
   rect = image.get_rect()
   rect.move_ip(xOffset,yOffset)
   sprite.rect = rect
   groupList[groupIndex].add(sprite)
def isWithinSquareByCoordinate(testx,testy,x1,y1,x2,y2):
   if testx > x1 and testx < x2 and testy > y1 and testy < y2:
     return True
   return False

# set up the colors
global BLACK
global GREY
global WHITE
global RED
global GREEN
global BLUE
global BGCOLOR

BLACK = (  0,   0,   0)
GREY =  ( 87,  87,  87)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOR = BLACK

