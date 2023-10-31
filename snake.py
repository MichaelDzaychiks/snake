import pygame

pygame.init()

ukuran_kotak = 20
lebar_grid = 450 // ukuran_kotak 
tinggi_grid = 450 // ukuran_kotak

lebar_jendela = lebar_grid * ukuran_kotak
tinggi_jendela = tinggi_grid * ukuran_kotak

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
def game_over_screen():
    pygame.display.flip()

def main():
    # Show game over screen
    game_over_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()