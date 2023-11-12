import unittest 
import pygame
from TicTacToe import TicTacToeGame

class TicTacToeTests(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game = TicTacToeGame()
    
    def tearDown(self):
        pygame.quit()

    def test_init_board(self):
        self.assertEqual(self.game.grid, [['', '', ''], ['', '', ''], ['', '', '']])

    def test_place_symbol(self):
        self.game.place_symbol(0, 0, 'X')
        self.assertEqual(self.game.grid[0][0], 'X')
    
    def test_take_turns(self):
        self.game.current_player = 'X'
        self.game.take_turn(0, 0)
        self.assertEqual(self.game.current_player, 'O')
    
    def test_check_win_row(self):
        self.game.grid = [['X','X','X'], ['-','-','-'], ['-','-','-']]
        self.assertTrue(self.game.check_win('X'))

    # Add more test cases for win conditions, ties, etc..

    def test_reset(self):
        self.game.grid = [['O','X','O'], ['X','O','X'], ['O','X','O']]
        self.game.reset()
        self.assertEqual(self.game.grid, [['', '', ''], ['', '', ''], ['', '', '']])

if __name__ == '__main__':
    unittest.main()