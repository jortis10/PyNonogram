from case import Case
from random import randint
import pygame
from PIL import Image
from numpy import*

class Game:

    def __init__(self,width,height):
        self.width = width
        self.height = height                                                                            
        self.heart = 3                                                                                  
        #self.cases = [[Case(0) for x in range(width*10)] for y in range(height*10)]
        self.cases = [[]]                           
        self.randomFill(30)                                                                             
        #self.fillFromImage("Assets/test.png")

    def randomFill(self,a):
        self.cases = [[Case(0) for x in range(self.width)] for y in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                n = randint(0,100)
                if n <= a:
                    self.cases[row][col].isPoint = 0
                else:
                    self.cases[row][col].isPoint = 1
        
    def fillFromImage(self, imagename):
        temp = Image.open(imagename)
        temp= temp.convert('1')      # Convert to black&white
        A = array(temp)             # Creates an array, white pixels==True and black pixels==False

        self.width = len(A[0])
        self.height = len(A)

        self.cases = [[Case(0) for x in range(self.width)] for y in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                print(row,end="")
                print(",",end="")
                print(col)
                if A[row][col]==True:
                    self.cases[row][col].isPoint = 0
                else:
                    self.cases[row][col].isPoint = 1

    

    def rowCount(self, row):
        n=0
        x = []

        for col in range(self.width):
            if self.cases[row][col].isPoint == 1:
                n+=1
            if self.cases[row][col].isPoint == 0:
                if n != 0:
                    x.append(n)
                n = 0
        if n !=0 :
            x.append(n)

        return x

    def columnCount(self, col):
        n=0
        x = []

        for row in range(self.height):
            if self.cases[row][col].isPoint == 1:
                n+=1
            if self.cases[row][col].isPoint == 0:
                if n != 0:
                    x.append(n)
                n = 0
        if n !=0 :
            x.append(n)

        return x
    
    def updateView(self, screen: pygame.Surface):
        self.displayCase(screen)
        self.displayBorder(screen)
        self.displayHeart(screen)
        self.displayCount(screen)

    def displayCase(self,screen: pygame.Surface):
        for row in range(self.height):
            for col in range(self.width):
                self.cases[row][col].updateCase()
                screen.blit(self.cases[row][col].image, ((col+3)*50,(row+3)*50))     #inverser


    
    def displayBorder(self,screen: pygame.Surface):
        image = pygame.image.load("Assets/border.png").convert_alpha()

        for column in range(self.width):
            screen.blit(image,((column+3)*50,0))

        image = pygame.transform.rotate(image, 90)
        for row in range(self.height):
            screen.blit(image,(0,(row+3)*50))

    def displayHeart(self,screen: pygame.Surface):
        image = pygame.image.load("Assets/heart.png").convert_alpha()
        image = pygame.transform.scale(image,(40,40))

        for k in range(self.heart):
            screen.blit(image,(k*50,0))

    def displayCount(self,screen: pygame.surface):
        font = pygame.font.SysFont("Assets/arial", 30)
        
        #display columns
        for col in range(self.width):
            x = self.columnCount(col)

            for row in range(len(x)):
                text = font.render(str(x[row]), True, (64, 64, 64))
                screen.blit(text,((col+3.3)*50,row*30))

        #display rows
        for row in range(self.height):
            x = self.rowCount(row)

            for col in range(len(x)):
                text = font.render(str(x[col]), True, (64, 64, 64))
                screen.blit(text,(col*30,(row+3.3)*50))






