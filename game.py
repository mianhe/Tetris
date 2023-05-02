import pygame
from block import Block

from playBoard import PlayBoard
from grid import Grid

NR_ROWS = 12
NR_COLS = 8

class Game:
       
    def __init__(self) -> None:
        self.__initTimer__()

    def __initTimer__(self):
        pygame.time.Clock()
        self.currentTickTime = 0
            
    def __isGameStarted__(self):
        return self.started
                
    def __resetGame__(self):
        self.playBoard = PlayBoard(NR_ROWS, NR_COLS)
        self.grid = Grid(NR_ROWS, NR_COLS)
        self.score = 0
        self.started = False
        self.playBoard.drawPlayBoard(self.score,self.grid)
        
    def __startOneRun__(self):        
        self.nextBlock = Block()
        self.__newBlock__()
        self.started = True
        
    def __rotateBlock__(self):
        self.grid.rotateBlock(self.ongoingBlock)
        
    def __moveBlockRight__(self):
        self.grid.moveBlockRight(self.ongoingBlock)

    def __moveBlockLeft__(self):
        self.grid.moveBlockLeft(self.ongoingBlock)

    def __moveBlockDown__(self):
        self.grid.moveBlockDown(self.ongoingBlock)
    
    def __isBlockTouchBottom__(self):
        return self.grid.isBlockTouchBottom(self.ongoingBlock) 
    
    def __settleBlock__(self):
        
        self.grid.settleBlock(self.ongoingBlock)
             
    def __clearFullRows__(self):
        rows = self.grid.clearFullRows()
        self.score += rows*rows
    
    def __newBlock__(self):
        self.ongoingBlock = self.nextBlock
        self.nextBlock = Block()        
    
    def __reachTickTime__(self):
        now  = pygame.time.get_ticks()
        if now - self.currentTickTime >= 1000:
            self.currentTickTime = pygame.time.get_ticks()
            return True
            
    def __isGameOver__(self):
        return self.grid.isGameOver()
    
    def __stopGame__(self):
        self.__resetGame__()
            
    def __drawBoard__(self):
        self.playBoard.drawPlayBoard(self.score,self.grid,
                                         self.ongoingBlock,self.nextBlock
                                         )
        
    def __responsEvent__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if not self.__isGameStarted__():
                    self.__startOneRun__()

                if event.key == pygame.K_LEFT:
                    self.__moveBlockLeft__()
                elif event.key == pygame.K_RIGHT:
                    self.__moveBlockRight__()
                elif event.key == pygame.K_DOWN:
                    self.__moveBlockDown__()
                elif event.key == pygame.K_UP:
                    self.__rotateBlock__()
                    
    def main(self):
        self.__resetGame__()

        while True:
            self.__responsEvent__()

            if not self.__isGameStarted__():
                continue                                 
            
            if self.__reachTickTime__():
                self.__moveBlockDown__()
                                
            if self.__isBlockTouchBottom__():
                self.__settleBlock__()
                self.__clearFullRows__()
                if self.__isGameOver__():
                    self.__stopGame__()
                else:
                    self.__newBlock__()                
                                                    
            self.__drawBoard__()

            
game = Game()
game.main()
        
        
        
    