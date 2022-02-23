
import pygame

pygame.init()
width=400
height=300
screen = pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption("bouncing ball")
bg = pygame.image.load("C:/Users/HP/OneDrive/Desktop/bg.jpg").convert_alpha()
x=150
y=290
vel=10
y1=10
x1=250
while True:    
  

    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
    ball1=pygame.draw.circle(screen,(255,0,0),(x,y),10)
    ball2=pygame.draw.circle(screen,(255,255,255),(x1,y1),10)
    if y==300:
        vel=-3
    elif  y==0:
        vel=3
    y=y+vel
    if y1==300:
        vel=3
    elif  y1==0:
        vel=-3
    y1=y1-vel
    
   
    pygame.display.update()
    clock.tick(50)