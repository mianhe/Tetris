import pygame
from block import Block

from playBoard import PlayBoard
from grid import Grid

NR_ROWS = 12
NR_COLS = 8

class Game:
       
    def __init__(self) -> None:
        pygame.time.Clock()
        self.currentTickTime = 0
                
    def startGame(self):        
        self.ongoingBlock = Block()
        self.nextBlock = Block()
        self.started = True
    
    def setGame(self):
        self.playBoard = PlayBoard(NR_ROWS, NR_COLS)
        #init the pygame clock
        self.ongoingBlock = Block('EMPTY')
        self.nextBlock = Block('EMPTY')
        self.grid = Grid(NR_ROWS, NR_COLS)
        self.score = 0
        self.started = False
        self.playBoard.drawPlayBoard(self.score,
                                        self.ongoingBlock,self.nextBlock,
                                        self.grid)

        
    def isGameStarted(self):
        return self.started
        
    def rotateBlock(self):
        self.grid.rotateBlock(self.ongoingBlock)
        
    def moveBlockRight(self):
        self.grid.moveBlockRight(self.ongoingBlock)

    def moveBlockLeft(self):
        self.grid.moveBlockLeft(self.ongoingBlock)

    def moveBlockDown(self):
        self.grid.moveBlockDown(self.ongoingBlock)
    
    def __responsEvent__(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if not self.isGameStarted():
                    self.startGame()
                    continue
                if event.key == pygame.K_LEFT:
                    self.moveBlockLeft()
                elif event.key == pygame.K_RIGHT:
                    self.moveBlockRight()
                elif event.key == pygame.K_DOWN:
                    self.moveBlockDown()
                elif event.key == pygame.K_UP:
                    self.rotateBlock()
    
    def isBlockTouchBottom(self):
        return self.grid.isBlockTouchBottom(self.ongoingBlock) 
    
    def settleBlock(self):
        
        self.grid.settleBlock(self.ongoingBlock)
             
    def isGameOver(self):
        return self.grid.isGameOver()
    
    def stopGame(self):
        self.setGame()
        
        
        
    
    def clearFullRows(self):
        rows = self.grid.clearFullRows()
        self.score += rows
    
    def newBlock(self):
        self.ongoingBlock = self.nextBlock
        self.nextBlock = Block()        
    
    def reachTickTime(self):
        # initial the pygame clock
        now  = pygame.time.get_ticks()
        if now - self.currentTickTime >= 1000:
            self.currentTickTime = pygame.time.get_ticks()
            return True
            
    
                    
    def main(self):

        self.setGame()
        while True:
            self.__responsEvent__()

            if not self.isGameStarted():
                continue                                 
            
            if self.reachTickTime():
                self.moveBlockDown()
                                
            if self.isBlockTouchBottom():
                self.settleBlock()
                self.clearFullRows()
                if self.isGameOver():
                    self.stopGame()
                else:
                    self.newBlock()                
                                                    
            self.__drawBoard__()

    def __drawBoard__(self):
        self.playBoard.drawPlayBoard(self.score,
                                         self.ongoingBlock,self.nextBlock,
                                         self.grid)
            
game = Game()
game.main()
        
        
        
    