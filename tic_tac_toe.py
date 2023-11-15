#References
#https://youtu.be/KBpfB1qQx8w?feature=shared
#https://youtu.be/vpodgih0X0Q?feature=shared
#Audio extract
#https://youtu.be/d1IHYpU6HdM?feature=shared
#https://youtu.be/MxASumLq1eY?feature=shared
#colour Code
#https://youtube.com/shorts/tSO6T_gR_Cs?feature=shared

import pygame
import sys
import pygame.mixer


# Initialize Pygame  for audio
pygame.mixer.init()

# Load the background music (provide the path to your audio file)
pygame.mixer.music.load(r"C:\Users\lenovo\Desktop\pygame\4 Minute Timer Relaxing Music Lofi Fish Background_k2iou3ecAFQ.mp3")

# Set the volume (0.0 to 1.0)
pygame.mixer.music.set_volume(1.0)

# Start playing the background music
pygame.mixer.music.play(-1)  # The '-1' argument loops the music indefinitely

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 350, 350
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 5
LINE_COLOR = (150, 0, 0)
PLAYER_X = "X"
PLAYER_O = "Y"

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the game grid
grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = PLAYER_X
tie = False


# Function to reset the game
def reset_game():
    global grid, current_player, tie
    grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    current_player = PLAYER_X
    tie = False




# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not tie and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if grid[row][col] == "":
                grid[row][col] = current_player
                current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O


    # Check for a winner
    winner = None
    for i in range(GRID_SIZE):
        if grid[i][0] == grid[i][1] == grid[i][2] != "":
            winner = grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != "":
            winner = grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        winner = grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        winner = grid[0][2]

    if not tie and all(all(cell != "" for cell in row) for row in grid) and winner is None:

        tie = True

    # Draw the background
    screen.fill((0,0,0))

    # Draw the grid lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

    # Draw X and O symbols
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == PLAYER_X:
                pygame.draw.line(screen, (0, 255, 0), (col * CELL_SIZE, row * CELL_SIZE),
                 ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)  # Lime color (0, 255, 0)
                pygame.draw.line(screen, (0, 255, 0), ((col + 1) * CELL_SIZE, row * CELL_SIZE),
                 (col * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)  # Lime color (0, 255, 0)

            elif grid[row][col] == PLAYER_O:
                pygame.draw.circle(screen, LINE_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2, LINE_WIDTH)

    # Display the winner or tie message
    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"   Player {winner} wins!", True, (250, 250, 250))  #  color (255, 255, 0)
        screen.blit(text, (80, HEIGHT // 2 - 18))
    elif tie:
        font = pygame.font.Font(None, 36)
        text = font.render("    It's a tie!", True, (250, 250, 250))  #  color (255, 255, 0)
        screen.blit(text, (80, HEIGHT // 2 - 18))
    
        if winner or tie:
            pygame.time.delay(10)
        

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()