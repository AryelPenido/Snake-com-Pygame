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

largura = 320
altura = 280
tamanho = 10

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None,15)

def texto(msg,cor):
    texto1 = font.render(msg,True,cor)
    fundo.blit(texto1,[largura/10, altura/2])
    
def cobra(CobraXY):
    for XY in CobraXY:
         pygame.draw.rect(fundo,black,[XY[0],XY[1],tamanho,tamanho])

def maca(pos_x,pos_y):
     pygame.draw.rect(fundo,red,[pos_x,pos_y,tamanho,tamanho])


def jogo():
    sair = True
    fimdejogo = False
    pos_x = randint(0,(largura-tamanho)/10)*10
    pos_y = randint(0,(altura-tamanho)/10)*10
    maca_x = randint(0,(largura-tamanho)/10)*10
    maca_y = randint(0,(altura-tamanho)/10)*10
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    Cobracomp = 1
    while sair:
        while fimdejogo:
            fundo.fill(white)
            texto("Fim de jogo, para continuiar tecle C ou S para sair",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sair= False
                     fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        
                        sair = True
                        fimdejogo = False
                        pos_x = randint(0,(largura-tamanho)/10)*10
                        pos_y = randint(0,(altura-tamanho)/10)*10
                        maca_x = randint(0,(largura-tamanho)/10)*10
                        maca_y = randint(0,(altura-tamanho)/10)*10
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []
                        Cobracomp = 1
                        
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sair= False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    pos_x -=10
                    velocidade_y = 0
                    velocidade_x =-tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    pos_x +=10
                    velocidade_y = 0
                    velocidade_x =tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    pos_y -=10
                    velocidade_x =0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN  and velocidade_y != -tamanho:
                    pos_y+=10
                    velocidade_x =0
                    velocidade_y = tamanho
        fundo.fill(white)
        pos_x+=velocidade_x
        pos_y+=velocidade_y

        if pos_x == maca_x and pos_y == maca_y:
             maca_x = randint(0,(largura-tamanho)/10)*10
             maca_y = randint(0,(altura-tamanho)/10)*10
             Cobracomp += 1
            
        if pos_x + tamanho > largura:
            pos_x=0
        if pos_x< 0:
            pos_x =largura-tamanho
        if pos_y + tamanho > altura:
            pos_y =0
        if pos_y <0:
            pos_y = altura-tamanho

            
        CobraInicio =[]
        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > Cobracomp:
            del CobraXY[0]
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo= True
        

        
        cobra(CobraXY)
        



        
        maca(maca_x,maca_y)
        pygame.display.update()
        relogio.tick(13)
        
jogo()

pygame.quit()


