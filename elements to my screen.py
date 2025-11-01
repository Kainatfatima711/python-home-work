import pygame


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Game Screen with Elements")


WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 74)
text = font.render("Hello, Pygame!", True, BLACK)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    # Draw a rectangle
    pygame.draw.rect(screen, BLUE, (300, 250, 200, 100))

    
    screen.blit(text, (230, 100))

    
    pygame.display.flip()


pygame.quit()