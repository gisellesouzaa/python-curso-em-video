#Cole o arquivo MP3 dentro da pasta do programa

import pygame
pygame.init()
pygame.mix.music.load('nomedoarquivo.mp3')
pygame.mixer.play()
pygame.event.wait()
 
