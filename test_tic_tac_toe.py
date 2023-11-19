#Reference
#https://www.youtube.com/watch?v=JJ9zZ8cyaEk
#https://www.youtube.com/watch?si=S12ryN5bv1VyYxj_&fbclid=IwAR3EglZae-QalhJKiVTTNoNgAC8r1--dlFEw5jJbwKqri_zDAtKsu1WZ4tU&v=v1MtwCPTmBI&feature=youtu.be
#https://www.youtube.com/watch?si=8V9ULoW1nwVc8gxe&fbclid=IwAR2PbuOp4PcRZH58C3yKuEWHB7Jm-NF-O4_I5IxBTolhVNIAqXLnNLJorM8&v=96mDQrlceEk&feature=youtu.be
#https://www.youtube.com/watch?v=mzlH8lp4ISA
#https://youtu.be/YbpKMIUjvK8?feature=shared

import unittest
import pygame
from unittest.mock import patch
#We just create a mock object, set its now() method to return our fixed date, then patch datetime.datetime to use our mock

#Initialize the screen
class TestGameScreen(unittest.TestCase):
    def setUp(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.GRID_SIZE = 3
        self.PLAYER_X = 'X'
        self.PLAYER_O = 'O'

    def test_game_initialization(self):
       # Initialize the game display and its set caption as Tic-Tac-Toe
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")

       # Initialize the game grid 3x3 
        grid = [["" for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        current_player = self.PLAYER_X
        tie = False

       # Assert that the screen is set correctly
        self.assertIsInstance(screen, pygame.Surface)
        self.assertEqual(screen.get_size(), (self.WIDTH, self.HEIGHT))

       # Assert that the grid is initialized correctly
        self.assertEqual(len(grid), self.GRID_SIZE)
        for row in grid:
            self.assertEqual(len(row), self.GRID_SIZE)
            self.assertEqual(row, ["" for _ in range(self.GRID_SIZE)])

       # Assert that the current player is set correctly
        self.assertEqual(current_player, self.PLAYER_X)

class TestGameCheckWinner(unittest.TestCase):
 #Set up test fixtures
 def setUp(self):
     self.GRID_SIZE = 3
     self.PLAYER_X = 'X'
     self.PLAYER_O = 'O'

 def test_check_winner(self):
     # Test horizontal win 
     grid = [["X", "X", "X"], ["", "", ""], ["", "", ""]]
     winner = self.check_winner(grid)
     self.assertEqual(winner, self.PLAYER_X)

     # Test vertical win
     grid = [["X", "", ""], ["X", "", ""], ["X", "", ""]]
     winner = self.check_winner(grid)
     self.assertEqual(winner, self.PLAYER_X)

     # Test diagonal win
     grid = [["X", "", ""], ["", "X", ""], ["", "", "X"]]
     winner = self.check_winner(grid)
     self.assertEqual(winner, self.PLAYER_X)

     # Test tie
     grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
     winner = self.check_winner(grid)
     self.assertEqual(winner, None)
    #Test the winner throught the grid
 def check_winner(self, grid):
     # Check rows
     for i in range(self.GRID_SIZE):
         if grid[i][0] == grid[i][1] == grid[i][2] != "":
             # If 3 values in a row are equal and not empty, we have a winner
             return grid[i][0]
    # Check columns
         if grid[0][i] == grid[1][i] == grid[2][i] != "":
             # If 3 values in a column are equal and not empty, we have a winner
             return grid[0][i]
     # Check first diagonal
     if grid[0][0] == grid[1][1] == grid[2][2] != "":
         # If 3 values on the diagonal are equal and not empty, we have a winner
         return grid[0][0]
     # Check second diagonal
     if grid[0][2] == grid[1][1] == grid[2][0] != "":
         # If 3 values on the anti-diagonal are equal and not empty, we have a winner
         return grid[0][2]
    # If no winner, check for empty cells
     if all(all(cell != "" for cell in row) for row in grid):
     # If no empty cells, it's a draw
         return None
         # No winner yet, keep playing

class TestGameDisplay(unittest.TestCase):
 # Set up test data
 def setUp(self):
   self.GRID_SIZE = 3
   self.PLAYER_X = 'X'
   self.PLAYER_O = 'O'
# Test displaying winner message
 def test_display_message(self):

    # Arrange test data
   winner = self.PLAYER_X
   tie = False
   # Act - call function
   message = self.display_message(winner, tie)
    # Assert correct message displayed
   self.assertEqual(message, f" Player {winner} wins!")

   # Test displaying tie message
   winner = None
   tie = True
    # Act - call function
   message = self.display_message(winner, tie)
    # Assert correct message displayed
   self.assertEqual(message, "  It's a tie!")
# Function to test
 def display_message(self, winner, tie):
   if winner:
       return f" Player {winner} wins!"
   elif tie:
       return "  It's a tie!"
   


if __name__ == '__main__':
   unittest.main()
