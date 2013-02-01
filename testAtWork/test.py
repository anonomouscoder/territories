import pygame, sys
from pygame.locals import *

def drawHex(xposition,yposition,length,color):
   diagonalLength = length*1.15
   hexgonWidth = 2*diagonalLength
   pygame.draw.polygon(DISPLAYSURF, color, ((xposition+diagonalLength, yposition), (xposition, yposition+diagonalLength), (xposition, yposition+diagonalLength+length), (xposition+diagonalLength,yposition+2*diagonalLength+length), (xposition+hexgonWidth,yposition+diagonalLength+length), (xposition+hexgonWidth,yposition+diagonalLength)))
   
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
BGCOLOR = WHITE

# draw on the surface object
DISPLAYSURF.fill(WHITE)
length = 50
drawHex(0,0,length,BLACK)
drawHex(1,1,49,WHITE)
drawHex(0,0,length,BLACK)
drawHex(1,1,49,WHITE)
drawHex(0,0,length,BLACK)
drawHex(1,1,49,WHITE)

# run the game loop
while True:
    mouseClicked = False
    DISPLAYSURF.fill(BGCOLOR) # drawing the window
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
        
    pygame.display.update()
