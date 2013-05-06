import pygame, sys
from pygame.locals import *
global length
global gap
global boardIndex
global columnWidth
global rowHeight

def drawSquare(xposition,yposition,length,color):
   pygame.draw.rect(DISPLAYSURF, color, (xposition,yposition,length,length))

# 
def drawSquareByIndex(index,length,color):
   print boardIndex[index]
   xposition,yposition = boardIndex[index]
   pygame.draw.rect(DISPLAYSURF, color, (xposition,yposition,length,length))
def isWithinSquareByCoordinate(testx,testy,x1,y1,x2,y2):
   if testx > x1 and testx < x2 and testy > y1 and testy < y2:
     return True
   return False
def isWithinSquareByIndex(testx,testy,index):
   if index == 1:
      x1 = 0
      y1 = 0
   elif index == 2:
      x1 = length + gap
      y1 = 0
   elif index == 3:
      x1 = 0
      y1 = length + gap
   elif index == 4:
      x1 = length + gap
      y1 = length + gap
   x2 = x1 + length
   y2 = y1 + length
   if testx > x1 and testx < x2 and testy > y1 and testy < y2:
     return True
   return False
def getColumnStart(columnIndex):
   columnStart = columnIndex - 1
pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOR = BLACK

# draw on the surface object
DISPLAYSURF.fill(BGCOLOR)
length = 50
gap = 3
columnWidth = length + gap
rowHeight = length + gap
x = 0
y = 0
boardIndex = {1:(0,0), 2:(x+columnWidth,y), 3:(x,y+rowHeight), 4:(x+columnWidth,y+rowHeight)}
drawSquareByIndex(1,length,WHITE)
drawSquareByIndex(2,length,WHITE)
drawSquareByIndex(3,length,WHITE)
drawSquareByIndex(4,length,WHITE)

# run the game loop
while True:
  mouseClicked = False
  #DISPLAYSURF.fill(BGCOLOR) # drawing the window
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == MOUSEMOTION:
      mousex, mousey = event.pos
    elif event.type == MOUSEBUTTONUP:
      mousex, mousey = event.pos
      mouseClicked = True
  if mouseClicked == True:
    for i in range(1,5):
      if isWithinSquareByIndex(mousex,mousey,i):
        drawSquareByIndex(i,length,RED)
    
  pygame.display.update()
