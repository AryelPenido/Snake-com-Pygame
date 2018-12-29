import pygame
from random import randint

white = (255,255,255)
black =(0,0,0)
red =(255,0,0)
green = (0,255,0)
blue = (0,0,255)

try:
    pygame.init()
except:
    print("o modulo não foi inicializado")

largura = 640
altura = 480
tamanho = 10
pos_x = randint(0,(largura-tamanho)/10)*10
pos_y = randint(0,(altura-tamanho)/10)*10
velocidade_x = 0
velocidade_y = 0

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x -=10
                velocidade_y = 0
                velocidade_x =-0.08
            if event.key == pygame.K_RIGHT:
                pos_x +=10
                velocidade_y = 0
                velocidade_x =0.08
            if event.key == pygame.K_UP:
                pos_y -=10
                velocidade_x =0
                velocidade_y = -0.08
            if event.key == pygame.K_DOWN:
                pos_y+=10
                velocidade_x =0
                velocidade_y = 0.08
    fundo.fill(white)
    pygame.draw.rect(fundo,black,[pos_x,pos_y,tamanho,tamanho])
    pos_x+=velocidade_x
    pos_y+=velocidade_y
    pygame.display.update()


pygame.quit()


