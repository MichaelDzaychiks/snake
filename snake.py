import pygame
import time
import random

pygame.init()

# Constants
ukuran_kotak = 20
lebar_grid = 450 // ukuran_kotak 
tinggi_grid = 450 // ukuran_kotak

lebar_jendela = lebar_grid * ukuran_kotak
tinggi_jendela = tinggi_grid * ukuran_kotak

paused = False

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pygame.display.set_mode((lebar_jendela, tinggi_jendela))
pygame.display.set_caption("Snake Game By MICHAEL AND HUTAO")

font = pygame.font.Font(None, 36)

def draw_grid():
    pass

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], ukuran_kotak, ukuran_kotak))

def draw_fruit(fruit):
    pygame.draw.rect(screen, RED, (fruit[0], fruit[1], ukuran_kotak, ukuran_kotak))

def draw_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (lebar_jendela - 150, 10))

def game_over_screen():
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over!", True, WHITE)
    play_again_text = font.render("Pencet Enter kl mw main lg", True, WHITE)
    screen.blit(game_over_text, (150, 150))
    screen.blit(play_again_text, (100, 200))
    pygame.display.flip()

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = RIGHT
    fruit = (200, 200)
    score = 0
    game_over = False

    clock = pygame.time.Clock()

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_RETURN:
                    snake = [(100, 100), (80, 100), (60, 100)]
                    direction = RIGHT
                    fruit = (200, 200)
                    score = 0
                    game_over = False

        if not game_over:
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0] * ukuran_kotak, head_y + direction[1] * ukuran_kotak)
            snake.insert(0, new_head)

            if snake[0] == fruit:
                score += 1
                fruit = (random.randint(0, lebar_grid - 1) * ukuran_kotak, random.randint(0, tinggi_grid - 1) * ukuran_kotak)
            else:
                snake.pop()

            if (
                snake[0][0] < 0
                or snake[0][0] >= lebar_jendela
                or snake[0][1] < 0
                or snake[0][1] >= tinggi_jendela
                or len(snake) != len(set(snake))
            ):
                game_over = True

            # Clear the screen
            screen.fill((0, 0, 0))

            draw_grid()
            draw_snake(snake)
            draw_fruit(fruit)
            draw_score(score)

            pygame.display.flip()

            clock.tick(10)

    game_over_screen()

    # Keep the game over screen displayed until the player presses Enter to play again
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                main()

if __name__ == "__main__":
    main()