import pygame, sys
from pygame.locals import *
from pygame import font
pygame.init()
global allFont
allFont = font.SysFont("monospace",15)
# set up the window
global MAINWINDOW
MAINWINDOW = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Territories')

def drawSquare(xposition,yposition,length,color):
   pygame.draw.rect(MAINWINDOW, color, (xposition,yposition,length,length))
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

