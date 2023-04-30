import copy
from block import Block


class Grid:
    def __init__(self,nrRows,nrCols):
        self.nrRows = nrRows
        self.nrCols = nrCols
        self.grid = [[0 for x in range(nrCols+2)] for y in range(nrRows+2)]
        self.grid[0] = [1 for x in range(nrCols+2)]
        self.grid[nrRows+1] = [1 for x in range(nrCols+2)]
        
        #set the left and right border
        for i in range(nrRows+2):
            self.grid[i][0] = 1
            self.grid[i][nrCols+1] = 1
            
            
    def moveBlockDown(self,block:Block):
        tempBlock = copy.copy(block)
        tempBlock.moveDown()
        if not self.__isCollision__(tempBlock):
            block.moveDown()
            
    def rotateBlock(self,block:Block):
        tempBlock = copy.copy(block)
        tempBlock.rotate()
        if not self.__isCollision__(tempBlock):
            block.rotate()

    def moveBlockRight(self,block:Block):
        tempBlock = copy.copy(block)
        tempBlock.moveRight()
        if not self.__isCollision__(tempBlock):
            block.moveRight()
    
    
    def moveBlockLeft(self,block:Block):
        tempBlock = copy.copy(block)
        tempBlock.moveLeft()
        if not self.__isCollision__(tempBlock):
            block.moveLeft()
    
    def isBlockTouchBottom(self,block:Block):
        tempBlock = copy.copy(block)
        tempBlock.moveDown()
        return self.__isCollision__(tempBlock)
            

    def settleBlock(self,block:Block):
        shape = block.getShape()
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j]:
                    self.__setValue__(i+block.y,j+block.x,1)
                    
    def clearFullRows(self):
        rowsCleared=0
        for row in range(self.nrRows):
                if self.__isFullRow__(row):
                    self.__clearRow__(row)
                    rowsCleared +=1
                    
        return rowsCleared
                                    
                
    def isGameOver(self):
        for col in range(self.nrCols):
            if self.__getValue__(1,col):
                return True
        return False
    
# move the rows above the row down by one    
    def __clearRow__(self,row):
        for r in range(row,0,-1):
            for col in range(self.nrCols):
                self.__setValue__(r,col,self.__getValue__(r-1,col))



    def __isCollision__(self,block:Block):
        shape = block.getShape()
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if self.__getValue__(i+block.y,j+block.x) and shape[i][j]:
                    return True
        return False
            
    def __setValue__(self,row,col,value):
        self.grid[row+1][col+1]=value
    
    def __getValue__(self,row,col):
        return self.grid[row+1][col+1]
            
    def __isFullRow__(self,row):
        for col in range(self.nrCols):
            if not self.__getValue__(row,col):
                return False
        return True
    
                
                
            