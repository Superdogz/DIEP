import pygame
 
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Game")
 

done = False
 

clock = pygame.time.Clock()
 

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    clock.tick(60)

pygame.quit()
