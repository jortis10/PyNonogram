import pygame

class Case:

    def __init__(self,caseType):
        self.caseType = caseType      #0 ou 1 ou 2(vide, point, croix)
        self.isPoint = 0
        self.image = ""
        self.isReveal = 0


    def updateCase(self):
        
        if self.caseType == 0:
            self.image = pygame.image.load("Assets/none.png").convert_alpha()
        elif self.caseType == 1:
            self.image = pygame.image.load("Assets/point.png").convert_alpha()
        elif self.caseType == 2 :
            self.image = pygame.image.load("Assets/cross.png").convert_alpha()

