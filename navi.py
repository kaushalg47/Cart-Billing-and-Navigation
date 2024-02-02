import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Supermarket Shelf Navigation")

shelves = [
    {"label": "A", "x": 50, "y": 50, "width": 50, "height": 200},
    {"label": "B", "x": 200, "y": 300, "width": 50, "height": 200},
    {"label": "C", "x": 400, "y": 100, "width": 50, "height": 200},
]

player_width = 20
player_height = 20

latitude = 37.7749
longitude = -122.4194

player_x = int((longitude + 180) / 360 * width)
player_y = int((90 - latitude) / 180 * height)

# Target rack for navigation
target_rack_label = "C"
target_rack = next(rack for rack in shelves if rack["label"] == target_rack_label)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for shelf in shelves:
        pygame.draw.rect(screen, BLACK, (shelf["x"], shelf["y"], shelf["width"], shelf["height"]))
        font = pygame.font.Font(None, 36)
        text = font.render(shelf["label"], True, BLACK)
        screen.blit(text, (shelf["x"] + 20, shelf["y"] + 20))

    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    if player_x < target_rack["x"]:
        player_x += 1
    elif player_x > target_rack["x"]:
        player_x -= 1

    if player_y < target_rack["y"]:
        player_y += 1
    elif player_y > target_rack["y"]:
        player_y -= 1

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
