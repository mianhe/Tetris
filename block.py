import random

BLOCK_SHAPES = {'I': [[1, 1, 1, 1]],
                'J': [[1, 0, 0],
                      [1, 1, 1]],
                'M':[[1,1]],
                'S':[[0,1,1],
                     [1,1,0]],
                'T':[[0,1,0],
                     [1,1,1]],
                'Z':[[1,1,0],
                     [0,1,1]],
                'O':[[1,1],
                     [1,1]]
                }    
 
class Block:
    def __init__(self,shapeID = 'random',x=0,y=0):        
        if shapeID == 'random':
            self.shapeID = random.choice(list(BLOCK_SHAPES.keys())) 
        else:
            self.shapeID= shapeID       
        self.x = x
        self.y = y
        self.rotation=0
        
    def moveDown(self):
        self.y += 1
    
    def moveRight(self):
        self.x += 1
    
    def moveLeft(self):
        self.x -= 1
         
    def getShape(self):
        if self.shapeID == 'EMPTY':
            return list([])
        
        shape = BLOCK_SHAPES[self.shapeID]
        for i in range(self.rotation):
            shape = list(zip(*shape[::-1]))
            
        return shape
        
    def rotate(self):
        self.rotation += 1
        self.rotation = self.rotation % 4
