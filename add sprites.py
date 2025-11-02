import pygame
import random


pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2


BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')


WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Bounce - Two Sprites")


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width, controlled=False):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.controlled = controlled
        self.speed = 4

       
        if not controlled:
            self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]
        else:
            self.velocity = [0, 0]

    def update(self):
        if not self.controlled:
            
            self.rect.move_ip(self.velocity)
            boundary_hit = False

            
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.velocity[0] = -self.velocity[0]
                boundary_hit = True
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.velocity[1] = -self.velocity[1]
                boundary_hit = True

            
            if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
        else:
           
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed

            
            self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
            self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

    def change_color(self):
        """Change sprite color randomly."""
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE, RED, GREEN]))


def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


all_sprites = pygame.sprite.Group()


auto_sprite = Sprite(WHITE, 30, 40)
auto_sprite.rect.x = random.randint(0, WIDTH - auto_sprite.rect.width)
auto_sprite.rect.y = random.randint(0, HEIGHT - auto_sprite.rect.height)
all_sprites.add(auto_sprite)


player_sprite = Sprite(RED, 30, 40, controlled=True)
player_sprite.rect.x = WIDTH // 2
player_sprite.rect.y = HEIGHT // 2
all_sprites.add(player_sprite)


bg_color = BLUE
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            auto_sprite.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    
    all_sprites.update()

    screen.fill(bg_color)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()