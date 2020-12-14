
import pygame

from gamescene_dfischer import Gamescene




def main():
    h = 600
    w = 800
    g = Gamescene(w,h)


    #pygame.mixer.music.load('assets/levelMusic.wav')
    #pygame.mixer.music.play(1) # -1 would make loop
    #pygame.mixer.music.set_volume(0.1)
    

    gameloop(h,w,g)

    pygame.mixer.music.stop()


def gameloop(h,w,g):
       
    play = True
    while(play):

              
        points = g.points

        g.update(points)

        g.setBackground(points)

        g.update(points)

        g.playGame(points)



        





        



        





main()
