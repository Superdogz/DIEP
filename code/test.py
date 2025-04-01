import os
import pygame

border_x, border_y = 2000, 2000
size = (1440, 780)

pygame.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode(size)

base_path = os.path.dirname(__file__)
assets_path = os.path.join(base_path, "..", "assets")

# Load images using the correct path
bg = pygame.image.load(os.path.join(assets_path, "background.svg"))
s = pygame.image.load(os.path.join(assets_path, "square.svg"))
t = pygame.image.load(os.path.join(assets_path, "triangle.svg"))
h = pygame.image.load(os.path.join(assets_path, "hexagon.svg"))
t_1 = pygame.image.load(os.path.join(assets_path, "main-tank.svg"))

print(os.path.join(assets_path, "background.png"))