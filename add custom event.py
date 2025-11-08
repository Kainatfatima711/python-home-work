import pygame
import random


pygame.init()


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Let's Level Up the Game!")


clock = pygame.time.Clock()


def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))


class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        self.image.fill(random_color())


sprite1 = ColorSprite(random_color(), 200, 200)
sprite2 = ColorSprite(random_color(), 400, 200)


sprites = pygame.sprite.Group(sprite1, sprite2)

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000) 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    
    screen.fill((30, 30, 30))
    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()