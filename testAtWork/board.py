import tile, drawUtils
from tile import tile
class Board:
   board = 0
   tileLength = 50
   gap = 3  
   columnWidth = tileLength + gap
   rowHeight = tileLength + gap
   oddRowOffset = 25
   def drawSquareByIndex(self,index,length,color):
      xposition,yposition = self.board[index].getCoordinate()
      drawUtils.drawSquare(xposition,yposition,length,color)
   def isWithinSquareByIndex(self,testx,testy,index):
      x1,y1 = self.board[index].getCoordinate()
      x2 = x1 + self.tileLength
      y2 = y1 + self.tileLength
      return drawUtils.isWithinSquareByCoordinate(testx,testy,x1,y1,x2,y2)
   def getColumnCoor(self,columnIndex,rowIndex):
      if rowIndex % 2 == 1:
         return (columnIndex - 1)*self.columnWidth + self.oddRowOffset
      else:
         return (columnIndex - 1)*self.columnWidth
   def getRowCoor(self,rowIndex):
      return (rowIndex -1)*self.rowHeight
   def getCoor(self,columnIndex,rowIndex):
      return (self.getColumnCoor(columnIndex,rowIndex),self.getRowCoor(rowIndex))
   def isPlayerAdjacent(self,index, player):
      color = drawUtils.WHITE
      if player == 1:
         color = drawUtils.RED
      else:
         color = drawUtils.BLUE
      goodTile = 0
      adjacentTiles = self.board[index].getAdjacencyMap()
      rtn = False   
      for i in adjacentTiles:
         if self.board[i].getStatus() == color:
            rtn = True
            goodTile = i
            break
      return rtn
   def __init__(self):
      self.board =  { 1: tile(self.getCoor(1,1),(1, 2, 3, 4)         ,drawUtils.WHITE,0),
                      2: tile(self.getCoor(2,1),(1, 2, 4, 5)         ,drawUtils.WHITE,0),
                      3: tile(self.getCoor(1,2),(1, 3, 4, 6)         ,drawUtils.WHITE,0),
                      4: tile(self.getCoor(2,2),(1, 2, 3, 4, 5, 6, 7),drawUtils.BLUE ,1),
                      5: tile(self.getCoor(3,2),(2, 4, 5, 7)         ,drawUtils.WHITE,0),
                      6: tile(self.getCoor(1,3),(3, 4, 6, 7, 8, 9)   ,drawUtils.WHITE,0),
                      7: tile(self.getCoor(2,3),(4, 5, 6, 7, 9,10)   ,drawUtils.WHITE,0),
                      8: tile(self.getCoor(1,4),(6, 8, 9,11)         ,drawUtils.WHITE,0),
                      9: tile(self.getCoor(2,4),(6, 7, 8, 9,10,11,12),drawUtils.RED  ,1),
                      10:tile(self.getCoor(3,4),(7, 9,10,12)         ,drawUtils.WHITE,0),
                      11:tile(self.getCoor(1,5),(8, 9,11,12)         ,drawUtils.WHITE,0),
                      12:tile(self.getCoor(2,5),(9,10,11,12)         ,drawUtils.WHITE,0)
                    }
   #