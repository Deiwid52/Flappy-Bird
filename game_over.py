import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Kolory
WHITE = (255, 255, 255)

def game_over():
    font = pygame.font.SysFont(None, 48)
    text = font.render("GAME OVER", True, (255, 0, 0))
    SCREEN.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # Opóźnienie, aby gracz zobaczył komunikat o przegranej
    pygame.quit()
    quit()