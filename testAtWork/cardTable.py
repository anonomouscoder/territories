import card, drawUtils

class CardTable:
   #variables
   cardWidth = 100
   cardHeight = 200
   def isWithinSquareByIndex(self,testx,testy,index):
      x1,y1 = self.listOfTiles[index].getCoordinate()
      x2 = x1 + self.cardWidth
      y2 = y1 + self.cardHeight
      return drawUtils.isWithinSquareByCoordinate(testx,testy,x1,y1,x2,y2)
   def getColumnCoor(self,columnIndex,rowIndex):
      if rowIndex % 2 == 1:
         return (columnIndex - 1)*self.columnWidth + self.oddRowOffset
      else:
         return (columnIndex - 1)*self.columnWidth + self.evenRowOffset
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
      adjacentTiles = self.listOfTiles[index].getAdjacencyMap()
      rtn = False   
      for i in adjacentTiles:
         if self.listOfTiles[i].getStatus() == color:
            rtn = True
            goodTile = i
            break
      return rtn
   def __init__(self):
      adjacencyMatrix = [(1, 2, 3, 4)         ,
                         (1, 2, 4, 5)         ,
                         (1, 3, 4, 6)         ,
                         (1, 2, 3, 4, 5, 6, 7),
                         (2, 4, 5, 7)         ,
                         (3, 4, 6, 7, 8, 9)   ,
                         (4, 5, 6, 7, 9,10)   ,
                         (6, 8, 9,11)         ,
                         (6, 7, 8, 9,10,11,12),
                         (7, 9,10,12)         ,
                         (8, 9,11,12)         ,
                         (9,10,11,12)         
                        ] 
      colorMatrix = [drawUtils.WHITE,
                     drawUtils.WHITE,
                     drawUtils.WHITE,
                     drawUtils.BLUE ,
                     drawUtils.WHITE,
                     drawUtils.WHITE,
                     drawUtils.WHITE,
                     drawUtils.WHITE,
                     drawUtils.RED  ,
                     drawUtils.WHITE,
                     drawUtils.WHITE,
                     drawUtils.WHITE
                    ]
      strengthMatrix = [0,
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0,
                        0
                       ]
      
      self.setBoard(adjacencyMatrix, colorMatrix, strengthMatrix)

   #
   #setters
   def setTileLength(self,length):
      self.tileLength = length
   def setGap(self, g):
      self.gap = g
   def setRowOffsets(self,odd,even):
      self.oddRowOffset = odd
      self.evenRowOffset = even
   def setRowColumnNumbers(self,odd,even):
      self.oddRowColumnNumber = odd
      self.evenRowColumnNumber = even
   #adjacencyMatrixArray :
   #  using 1-indexing, list indices of tiles that are adjacent to this one (include self)
   #colorArray :
   #  using the drawUtils globals (or a set of 3 integers range = 0-255), provide a color for each tile
   #strengthArray :
   #  provide a integer that represents the strength of the tile
   def setBoard(self, adjacencyMatrixArray, colorArray, strengthArray):
      validLength = (self.numberOfRows/2)*self.evenRowColumnNumber + (self.numberOfRows/2 + self.numberOfRows % 2)*self.oddRowColumnNumber
      
      if len(adjacencyMatrixArray) !=  validLength or len(colorArray) != validLength or len(strengthArray) != validLength:
         print "invalid lengths. valid length = " + str(validLength) + ", invalid length = " + str(len(adjacencyMatrixArray)) + " or " + str(len(colorArray)) + " or " + str(len(strengthArray))
         return -1
         
      columnIndex = 0
      rowIndex = 1
      
      self.listOfTiles = {}
      for i in range(1,validLength+1):
         columnIndex = columnIndex + 1
         if (rowIndex % 2 == 1 and columnIndex > self.oddRowColumnNumber) or (rowIndex % 2 == 0 and columnIndex > self.evenRowColumnNumber):
            columnIndex = 1
            rowIndex = rowIndex + 1
         self.listOfTiles[i] = tile(self.getCoor(columnIndex,rowIndex), adjacencyMatrixArray[i-1], colorArray[i-1], strengthArray[i-1])
   #