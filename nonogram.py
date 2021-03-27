import pygame
from game import Game
import cProfile

width = 10
height = 10

def main():
    #initialisation pygame
    pygame.init()

    jeu = Game(width,height)

    #Generation de la fenêtre
    screen = pygame.display.set_mode(((jeu.width+3)*50, (jeu.height+3)*50))
    icon = pygame.image.load("Assets/icon.png").convert()
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Nonogram")
    screen.fill([255,255,255])

    running = True

    while running and jeu.heart > 0:
        for event in pygame.event.get():

            x = int((pygame.mouse.get_pos()[0])/50)-3
            y = int((pygame.mouse.get_pos()[1])/50)-3

            if event.type == pygame.QUIT:
                running = False

            if x >=0 and y >= 0:
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if pygame.mouse.get_pressed(3) == (True,False,False):
                        if jeu.cases[y][x].isPoint == 1:
                            if jeu.cases[y][x].caseType == 1:
                                jeu.cases[y][x].caseType = 0
                            else:
                                jeu.cases[y][x].caseType = 1
                            jeu.cases[y][x].isReveal = 1
                        else:
                            jeu.heart-=1
                    if pygame.mouse.get_pressed(3) == (False,False,True):
                        if jeu.cases[y][x].isPoint == 0:
                            if jeu.cases[y][x].caseType == 2:
                                jeu.cases[y][x].caseType = 0
                            else:
                                jeu.cases[y][x].caseType = 2
                        else:
                            jeu.heart-=1
                
            
        #Routine de frame
        screen.fill([255,255,255])
        jeu.updateView(screen)
        pygame.display.flip()

    #Fermeture du jeu
    pygame.quit()


if __name__ == '__main__':
    main()

