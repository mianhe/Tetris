import pygame
from block import Block
from grid import Grid

CELL_SIZE = 40
BORDER = CELL_SIZE

NEXT_BLOCK_BOARD_WIDTH = CELL_SIZE*6
NEXT_BLOCK_BOARD_HEIGHT = CELL_SIZE*4

SCORE_BOARD_HEIGHT = CELL_SIZE
SCORE_BOARD_WIDTH = NEXT_BLOCK_BOARD_WIDTH

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED=(255,0,0)

class PlayBoard:
    def drawPlayBoard(self,score,grid,ongoingBlock=None,nextBlock=None):
        pygame.draw.rect(self.palyBoard, (0,0,0), (0, 0, self.palyBoard.get_width(), self.palyBoard.get_height()), 0)
        
        self.__drawScoreBoard__(score)
        self.__drawOngoingBlockBoard__(ongoingBlock)
        self.__drawNextBlockBoard__(nextBlock)
        self.__drawSettledBlock__(grid)
        self.__drawGrid__()
        
        pygame.display.update()

    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.__createScreen__()

    def __createScreen__(self):
        screenWidth = (self.cols+1) * CELL_SIZE + 2 * BORDER + NEXT_BLOCK_BOARD_WIDTH
        screenHeight = self.rows * CELL_SIZE + 2 * BORDER
        self.palyBoard = pygame.display.set_mode((screenWidth, screenHeight))    
    
    def __drawGrid__(self):
        for i in range(self.rows+1):
            pygame.draw.line(self.palyBoard, WHITE, (BORDER, BORDER+i*CELL_SIZE), \
                (BORDER+self.cols*CELL_SIZE, BORDER+i*CELL_SIZE), 1)
        for i in range(self.cols+1):
            pygame.draw.line(self.palyBoard, WHITE, (BORDER+i*CELL_SIZE, BORDER), \
                (BORDER+i*CELL_SIZE, BORDER+self.rows*CELL_SIZE), 1)
    
    def __drawCell__(self, x, y, color):
        pygame.draw.rect(self.palyBoard, color, (BORDER+x*CELL_SIZE, BORDER+y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
    
    def __drawCellInNextBoard__(self, x, y, color):
        pygame.draw.rect(self.palyBoard, color, (BORDER+x*CELL_SIZE+CELL_SIZE*(self.cols+2), BORDER+(y+1)*CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)

    def __drawGridInNextBoar__d(self):
        for i in range(5):
            pygame.draw.line(self.palyBoard, WHITE, (BORDER+(self.cols+1)*CELL_SIZE, BORDER+i*CELL_SIZE), \
                (BORDER+(self.cols+1)*CELL_SIZE+NEXT_BLOCK_BOARD_WIDTH, BORDER+i*CELL_SIZE), 1)
        for i in range(7):
            pygame.draw.line(self.palyBoard, WHITE, (BORDER+(self.cols+1)*CELL_SIZE+i*CELL_SIZE, BORDER), \
                (BORDER+(self.cols+1)*CELL_SIZE+i*CELL_SIZE, BORDER+4*CELL_SIZE), 1)
                    
    def __drawBlock__(self,block:Block):
        shape = block.getShape()
        
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j]==1:
                    self.__drawCell__(block.x+j,block.y+i,RED)

    def __drawBlockInNextBoard__(self,nextBlock:Block):
        shape = nextBlock.getShape()
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j]==1:
                    self.__drawCellInNextBoard__(nextBlock.x+j,nextBlock.y+i,RED)

    def __drawNextBlockBoard__(self,nextBlock = None):
        pygame.draw.rect(self.palyBoard, GRAY, (BORDER+(self.cols+1)*CELL_SIZE, BORDER, NEXT_BLOCK_BOARD_WIDTH, NEXT_BLOCK_BOARD_HEIGHT), 0)
        if nextBlock:
            self.__drawBlockInNextBoard__(nextBlock)
        self.__drawGridInNextBoar__d()
        
    def __drawOngoingBlockBoard__(self,ongoingBlock):
        # pygame.draw.rect(self.palyBoard, GRAY, (BORDER, BORDER, self.cols*CELL_SIZE, self.rows*CELL_SIZE), 0)
        if ongoingBlock:
            self.__drawBlock__(ongoingBlock)
    
    #draw the score board, bottom allign with the bottom horizontal line, left allign with the next block board
    def __drawScoreBoard__(self,score=0):
        pygame.draw.rect(self.palyBoard, GRAY, (BORDER+(self.cols+1)*CELL_SIZE, 
                                                BORDER+self.rows*CELL_SIZE-SCORE_BOARD_HEIGHT, 
                                                SCORE_BOARD_WIDTH, SCORE_BOARD_HEIGHT), 0)
        #write score to the board
        pygame.font.init()
        self.palyBoard.blit(pygame.font.SysFont('arial', 20).render('Score: %d' % score, True, RED), 
                   (BORDER+(self.cols+1)*CELL_SIZE+10, BORDER+self.rows*CELL_SIZE-SCORE_BOARD_HEIGHT+10))

    def __drawSettledBlock__(self,grid:Grid):
        for i in range(self.rows):
            for j in range(self.cols):
                if grid.__getValue__(i,j):
                    self.__drawCell__(j,i,RED)
                 
        
        
        