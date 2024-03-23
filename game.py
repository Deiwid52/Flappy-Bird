import pygame
import random
from bird import Bird
from Obstacle import Obstacle


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
RED = (255, 0, 0)


def game_over(score):
    font = pygame.font.SysFont(None, 48)
    text = font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {score}", True, (0, 255, 0))
    SCREEN.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + text.get_height() // 2 + 10))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    quit()


def main():
    pygame.init()
    clock = pygame.time.Clock()

    background = pygame.image.load("background.jpg")
    background_rect = background.get_rect()

    bird = Bird()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)


    obstacles = pygame.sprite.Group()


    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()


        if len(obstacles) == 0 or obstacles.sprites()[-1].rect.right < SCREEN_WIDTH - 200:
            obstacle_height = random.randint(50, 300)
            obstacle = Obstacle(SCREEN_WIDTH, 0, 50, obstacle_height)
            obstacle2 = Obstacle(SCREEN_WIDTH, obstacle_height + 200, 50, SCREEN_HEIGHT - (obstacle_height + 200))
            obstacles.add(obstacle, obstacle2)
            all_sprites.add(obstacle, obstacle2)


        all_sprites.update()


        if bird.rect.top <= 0 or bird.rect.bottom >= SCREEN_HEIGHT:
            game_over(score)

        hits = pygame.sprite.spritecollide(bird, obstacles, False)
        if hits:
            game_over(score)


        for obstacle in obstacles:
            if obstacle.off_screen():
                obstacles.remove(obstacle)
                all_sprites.remove(obstacle)
                score += 1

        # Background
        SCREEN.blit(background, background_rect)
        background_rect.x -= 1
        if background_rect.right <= SCREEN_WIDTH:
            background_rect.x = 0

        all_sprites.draw(SCREEN)

        #Score
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"{score}", True, (0, 255, 0))
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

