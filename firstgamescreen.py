import pygame


pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game Screen")


background_color = (200, 162, 200)  
text_color = (255, 255, 255)      


font = pygame.font.Font(None, 48)
text = font.render("Welcome to My First Game!", True, text_color)
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  


    screen.fill(background_color)

    
    screen.blit(text, text_rect)

    
    pygame.display.flip()


pygame.quit()