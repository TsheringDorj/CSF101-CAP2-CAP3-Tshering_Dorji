import unittest
from tic_tac_toe import TicTacToeGame

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToeGame()

    def test_place_marker(self):
        self.game.place_marker(1, 1)
        self.assertEqual(self.game.board[1][1], 'X')
        
        self.game.place_marker(2, 2)
        self.assertEqual(self.game.board[2][2], 'O')

    def test_get_winner(self):
        # Test row win
        self.game.board = [['X','X','X'],
                           ['O','',''],
                           ['','','']]
        self.assertEqual(self.game.get_winner(), 'X')
        
        # Test column win 
        self.game.board = [['','O',''],
                           ['','O',''],
                           ['','O','']]
        self.assertEqual(self.game.get_winner(), 'O')