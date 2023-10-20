import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 5
LINE_COLOR = (255, 255, 255)
PLAYER_X = "X"
PLAYER_O = "O"

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the game grid
grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = PLAYER_X
winner = None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if winner is None and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if grid[row][col] == "":
                grid[row][col] = current_player
                current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

    # Check for a winner
    for i in range(GRID_SIZE):
        if grid[i][0] == grid[i][1] == grid[i][2] != "":
            winner = grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != "":
            winner = grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        winner = grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        winner = grid[0][2]

    # Draw the background
    screen.fill((0, 0, 0))

    # Draw the grid lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

    # Draw X and O symbols
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == PLAYER_X:
                pygame.draw.line(screen, LINE_COLOR, (col * CELL_SIZE, row * CELL_SIZE),
                                 ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, ((col + 1) * CELL_SIZE, row * CELL_SIZE),
                                 (col * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
            elif grid[row][col] == PLAYER_O:
                pygame.draw.circle(screen, LINE_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2, LINE_WIDTH)

    # Display the winner
    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player {winner} wins!", True, LINE_COLOR)
        screen.blit(text, (50, HEIGHT // 2 - 18))

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()
