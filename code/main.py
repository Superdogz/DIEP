import pygame
import math
import random

border_x, border_y = 2000, 2000
size = (1440, 780)


pygame.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode(size)



bg = pygame.image.load("assets/background.svg")
s = pygame.image.load("assets/square.svg")
t = pygame.image.load("assets/triangle.svg")
h = pygame.image.load("assets/hexagon.svg")
t_1 =  pygame.image.load("assets/main-tank.svg")

class Player:
    def __init__(self, x, y, type, health = 100, x_acc=0, y_acc=0, angle=0, score=0, recoil = 1, regen=1, max=1, body=1, speed=1, penetration=1, damage=1, reload=1, movement=1, die = 0):
        self.x = x
        self.y = y
        self.x_acc = x_acc
        self.y_acc = y_acc
        self.type = type
        self.angle = angle
        self.score = score
        self.recoil = recoil
        self.regen = regen
        self.max = max
        self.health = health
        self.body = body
        self.speed = speed
        self.penetration = penetration
        self.damage = damage
        self.reload = reload
        self.movement = movement
        self.die = die

    def draw(self):
        if self.type == 1:
            scaled_image = pygame.transform.scale(t_1, (100, 100))
            rotated_image = pygame.transform.rotate(scaled_image, math.degrees(self.angle))
            rotated_rect = rotated_image.get_rect(center=(720, 390))
            screen.blit(rotated_image, rotated_rect)
    
    def death(self):
        self.die += 1
        if self.die >= 15:
            return 

        fade_surface = pygame.Surface((24,24), pygame.SRCALPHA) 
        fade_surface.set_alpha(max(0, 255 - self.die * 15)) 

        scaled_image = pygame.transform.scale(t_1, (100+self.die/3, 100+self.die/3))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(720, 390))
        screen.blit(rotated_image, rotated_rect)

    
    def hp_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (720-20, 390+30, 40, 5))
        pygame.draw.rect(screen, (0, 255, 0), (720-20, 390+30, 40 * self.health/100, 5))

class P_Bullet:
    def __init__(self, x, y, angle, speed, tank, size = 8, die = 0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.tank = tank
        self.size = size
        self.die = die
    def draw(self):
        pygame.draw.circle(screen, (10, 120, 160), (720+(self.x-player.x), 390+(self.y-player.y)), self.size+2)
        pygame.draw.circle(screen, (40, 180, 230), (720+(self.x-player.x), 390+(self.y-player.y)), self.size)
    def death(self):
        self.die += 1
        if self.die >= 15:
            p_bullets.remove(self)
            return 

        fade_surface = pygame.Surface((24, 24), pygame.SRCALPHA) 
        fade_surface.set_alpha(max(0, 255 - self.die * 15)) 

        pygame.draw.circle(fade_surface, (10, 120, 160), (12, 12), self.size+2+self.die/3) 
        screen.blit(fade_surface, (720 + (self.x - player.x)-self.size, 390 + (self.y - player.y)-self.size))  

        pygame.draw.circle(fade_surface, (40, 180, 230), (12,12), self.size+self.die/3) 
        screen.blit(fade_surface, (720 + (self.x - player.x)-self.size, 390 + (self.y - player.y)-self.size))  

class Square:
    def __init__(self, x, y, angle, health = 10, die = 0):
        self.x = x
        self.y = y
        self.angle = angle
        self.health = health
        self.die = die
    def draw(self):
        scaled_image = pygame.transform.scale(s, (40, 40))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(720+self.x-player.x, 390-(player.y-self.y)))
        screen.blit(rotated_image, rotated_rect)
    def hp_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (720+self.x-player.x-20, 390-(player.y-self.y)+30, 40, 5))
        pygame.draw.rect(screen, (0, 255, 0), (720+self.x-player.x-20, 390-(player.y-self.y)+30, 40 * self.health/10, 5))
    def death(self):
        self.die += 1
        if self.die >= 15:
            squares.remove(self)
            return 
        
        fade_surface = pygame.Surface((24,24), pygame.SRCALPHA) 
        fade_surface.set_alpha(max(0, 255 - self.die * 15)) 

        scaled_image = pygame.transform.scale(s, (40+self.die/2, 40+self.die/2))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(720+self.x-player.x, 390-(player.y-self.y)))
        screen.blit(rotated_image, rotated_rect)

class Triangle:
    def __init__(self, x, y, angle, health = 30, die = 0):
        self.x = x
        self.y = y
        self.angle = angle
        self.health = health
        self.die = die
    def draw(self):
        scaled_image = pygame.transform.scale(t, (50, 50))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(720+self.x-player.x, 390-(player.y-self.y)))
        screen.blit(rotated_image, rotated_rect)
    def hp_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (720+self.x-player.x-20, 390-(player.y-self.y)+30, 40, 5))
        pygame.draw.rect(screen, (0, 255, 0), (720+self.x-player.x-20, 390-(player.y-self.y)+30, 40 * self.health/30, 5))
    def death(self):
        self.die += 1
        if self.die >= 15:
            triangles.remove(self)
            return 
        
        fade_surface = pygame.Surface((24,24), pygame.SRCALPHA) 
        fade_surface.set_alpha(max(0, 255 - self.die * 15)) 

        scaled_image = pygame.transform.scale(t, (50+self.die/2, 50+self.die/2))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(720+self.x-player.x, 390-(player.y-self.y)))
        screen.blit(rotated_image, rotated_rect)

class Hexagon:
    def __init__(self, x, y, angle, health = 60, die = 0):
        self.x = x
        self.y = y
        self.angle = angle
        self.health = health
        self.die = die
    def draw(self):
        scaled_image = pygame.transform.scale(h, (60, 60))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(720+self.x-player.x, 390-(player.y-self.y)))
        screen.blit(rotated_image, rotated_rect)
    def hp_bar(self):
        pygame.draw.rect(screen, (255, 0, 0), (720+self.x-player.x-20, 390-(player.y-self.y)+30, 40, 5))
        pygame.draw.rect(screen, (0, 255, 0), (720+self.x-player.x-20, 390-(player.y-self.y)+30, 40 * self.health/60, 5))
    def death(self):
        self.die += 1
        if self.die >= 15:
            hexagons.remove(self)
            return 
        
        fade_surface = pygame.Surface((24,24), pygame.SRCALPHA) 
        fade_surface.set_alpha(max(0, 255 - self.die * 15)) 

        scaled_image = pygame.transform.scale(h, (60+self.die/2, 60+self.die/2))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(720+self.x-player.x, 390-(player.y-self.y)))
        screen.blit(rotated_image, rotated_rect)



def createBackground(x,y):
    # 9 tiles
    screen.blit(bg, ((-x)%1500, (-y)%1500))
    screen.blit(bg, ((-x)%1500+1500, (-y)%1500))
    screen.blit(bg, ((-x)%1500-1500, (-y)%1500))
    screen.blit(bg, ((-x)%1500, (-y)%1500+1500))
    screen.blit(bg, ((-x)%1500, (-y)%1500-1500))
    screen.blit(bg, ((-x)%1500+1500, (-y)%1500-1500))
    screen.blit(bg, ((-x)%1500+1500, (-y)%1500+1500))
    screen.blit(bg, ((-x)%1500-1500, (-y)%1500-1500))
    screen.blit(bg, ((-x)%1500-1500, (-y)%1500+1500))
    if player.x >= border_x-720:
        pygame.draw.rect(screen, (100, 100, 100), (720+border_x-player.x,0,1000,780))
    if player.x <= -border_x+720:
        pygame.draw.rect(screen, (100, 100, 100), (720-(player.x+border_x)-1000,0,1000,780))
    if player.y >= border_x-390:
        pygame.draw.rect(screen, (100, 100, 100), (0,390+(border_y-player.y),1440,1000))
    if player.y <= -border_y+390:
        pygame.draw.rect(screen, (100, 100, 100), (0,390-(player.y+border_y)-1000,1440,1000))

player = Player(0,0,1)
done = False
state = 1
tick = 0
clock = pygame.time.Clock()
p_bullets = []
shapes = 20
squares = []
triangles = []
hexagons = []

for i in range(shapes):
    squares.append(Square(random.randint(-border_x+50,border_x-50),random.randint(-border_y+50,border_y-50),math.degrees(random.randint(1,360))))
    triangles.append(Triangle(random.randint(-border_x+50,border_x-50),random.randint(-border_y+50,border_y-50),math.degrees(random.randint(1,360))))
    hexagons.append(Hexagon(random.randint(-border_x+50,border_x-50),random.randint(-border_y+50,border_y-50),math.degrees(random.randint(1,360))))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    createBackground(player.x, player.y)
    
    pressed = False
    # player angle
    player.angle = math.atan2(390-pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[0]-720)

    #take user inputs
    keys = pygame.key.get_pressed()

    if player.x > -border_x+20 :
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:   # Move left
            if player.x_acc > -player.movement-2:
                player.x_acc -= 0.1
                pressed = True
    else:
        player.x_acc = 0
        player.x += 1

    if player.x < border_x-20:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Move right
            if player.x_acc < 2+player.movement:
                player.x_acc += 0.1
                pressed = True
    else:
        player.x_acc = 0
        player.x -= 1

    if player.y > -border_y+20:
        if keys[pygame.K_UP] or keys[pygame.K_w]:     # Move up
            if player.y_acc > -player.movement-2:
                player.y_acc -= 0.1
                pressed = True
    else:
        player.y_acc = 0
        player.y += 1

    if player.y < border_y-20:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:   # Move down
            if player.y_acc < 2+player.movement:
                player.y_acc += 0.1
                pressed = True
    else:
        player.y_acc = 0
        player.y -= 1
        
    #add decceleration
    if pressed == False:
        if player.y_acc > 0:
            player.y_acc -= 0.1
        if player.y_acc < 0:
            player.y_acc += 0.1
        if player.x_acc > 0:
            player.x_acc -= 0.1
        if player.x_acc < 0:
            player.x_acc += 0.1
        
        if player.x_acc > 3+player.movement:
            player.x_acc -= 0.2
        if player.x_acc < -(3+player.movement):
            player.x_acc += 0.2
        if player.y_acc > 3+player.movement:
            player.y_acc -= 0.2
        if player.y_acc < -(3+player.movement):
            player.y_acc += 0.2

    #add bullets
    if tick % (65-5*player.reload) == 0:
        p_bullets.append(P_Bullet(player.x+math.cos(player.angle)*50, player.y-math.sin(player.angle)*50, player.angle, 5+player.speed, player.type))
        player.x_acc += -1 * player.recoil * math.cos(player.angle)
        player.y_acc -= -1 * player.recoil * math.sin(player.angle)
    # draw squares
    for square in squares:
        if square.die == 0:
            if math.sqrt(pow(square.x-player.x,2)+pow(square.y-player.y,2)) <= 40 and square.die == 0: # player collision
                player.health -= 2
                square.health -= 2
                player.x_acc = 0
                player.y_acc = 0
                #recoil
                player.x_acc += math.cos(math.atan2(player.y-square.y,square.x-player.x))*math.log(8*math.sqrt(pow(square.x-player.x,2)+pow(square.y-player.y,2)),2)/3
                player.y_acc += math.sin(math.atan2(player.y-square.y,square.x-player.x))*math.log(8*math.sqrt(pow(square.x-player.x,2)+pow(square.y-player.y,2)),2)/3
        #delete square if health is equal to 0
        if square.health <= 0:
            square.health = 0
            square.death()
        else:
            if square.health != 10:
                square.hp_bar()
            square.draw()
    # draw triangles
    for triangle in triangles:
        if triangle.die == 0:
            if math.sqrt(pow(triangle.x-player.x,2)+pow(triangle.y-player.y,2)) <= 40 and triangle.die == 0: # player collision
                player.health -= 2.5
                triangle.health -= 2.5
                player.x_acc = 0
                player.y_acc = 0
                #recoil
                player.x_acc += math.cos(math.atan2(player.y-triangle.y,triangle.x-player.x))*math.log(8*math.sqrt(pow(triangle.x-player.x,2)+pow(triangle.y-player.y,2)),2)/3
                player.y_acc += math.sin(math.atan2(player.y-triangle.y,triangle.x-player.x))*math.log(8*math.sqrt(pow(triangle.x-player.x,2)+pow(triangle.y-player.y,2)),2)/3
        # delete triangle if health is equal to 0
        if triangle.health <= 0:
            triangle.health = 0
            triangle.death()
        else:
            if triangle.health != 30:
                triangle.hp_bar()
            triangle.draw()
    # draw hexagons
    for hexagon in hexagons:
        if hexagon.die == 0:
            if math.sqrt(pow(hexagon.x-player.x,2)+pow(hexagon.y-player.y,2)) <= 40 and hexagon.die == 0: # player collision
                player.health -= 3
                hexagon.health -= 3
                player.x_acc = 0
                player.y_acc = 0
                #recoil
                player.x_acc += math.cos(math.atan2(player.y-hexagon.y,hexagon.x-player.x))*math.log(8*math.sqrt(pow(hexagon.x-player.x,2)+pow(hexagon.y-player.y,2)),2)/3
                player.y_acc += math.sin(math.atan2(player.y-hexagon.y,hexagon.x-player.x))*math.log(8*math.sqrt(pow(hexagon.x-player.x,2)+pow(hexagon.y-player.y,2)),2)/3
        # delete hexagon if health is equal to 0
        if hexagon.health <= 0:
            hexagon.health = 0
            hexagon.death()
        else:
            if hexagon.health != 60:
                hexagon.hp_bar()
            hexagon.draw()
    # add squares
    if len(squares) < shapes:
        if random.randint(shapes-30,len(squares)) == shapes-30:
            squares.append(Square(random.randint(-border_x+50,border_x-50),random.randint(-border_y+50,border_y-50),random.randint(1,360)))
    # add triangles
    if len(triangles) < shapes:
        if random.randint(shapes-30,len(triangles)) == shapes-30:
            triangles.append(Triangle(random.randint(-border_x+50,border_x-50),random.randint(-border_y+50,border_y-50),random.randint(1,360)))
    # add hexagons
    if len(hexagons) < shapes:
        if random.randint(shapes-30,len(hexagons)) == shapes-30:
            hexagons.append(Hexagon(random.randint(-border_x+50,border_x-50),random.randint(-border_y+50,border_y-50),random.randint(1,360)))


    #collision checks for player bullets
    for bullet in p_bullets:
        bullet.x += math.cos(bullet.angle)*bullet.speed
        bullet.y -= math.sin(bullet.angle)*bullet.speed
        #border
        if (bullet.x >= border_x or bullet.x <= -border_x or bullet.y >= border_y or bullet.y <= -border_y) and bullet.die == 0:
            bullet.speed -= 1
        #square
        for square in squares:
            if abs(square.x-bullet.x) > 1000:
                pass
            else:
                if math.sqrt(pow(square.x-bullet.x,2)+pow(square.y-bullet.y,2)) <= bullet.size+20 and bullet.die == 0:
                    bullet.speed -= 2/player.penetration
                    square.health -= 2*player.damage
        #triangle
        for triangle in triangles:
            if abs(triangle.x-triangle.x) > 1000:
                pass
            else:
                if math.sqrt(pow(triangle.x-bullet.x,2)+pow(triangle.y-bullet.y,2)) <= bullet.size+20 and bullet.die == 0:
                    bullet.speed -= 2/player.penetration
                    triangle.health -= 2*player.damage
        
        #hexagon
        for hexagon in hexagons:
            if abs(hexagon.x-hexagon.x) > 1000:
                pass
            else:
                if math.sqrt(pow(hexagon.x-bullet.x,2)+pow(hexagon.y-bullet.y,2)) <= bullet.size+20 and bullet.die == 0:
                    bullet.speed -= 2/player.penetration
                    hexagon.health -= 2*player.damage

        

        # delete bullet if speed is equal to 0
        if bullet.speed <= 0:
            bullet.speed = 0
            bullet.death()
        else:
            bullet.draw()

        



    #update the player pos
    player.x += player.x_acc            
    player.y += player.y_acc
    player.health += player.regen/30
    if player.health > 100:
        player.health = 100
    if player.health <= 0:
        player.death()
    else:
        if player.health == 100:
            player.draw()   
        else:
            player.draw()
            player.hp_bar()


    tick += 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
