import unittest
from tic_tac_toe import grid, current_player, tie, reset_game

class TestTicTacToe(unittest.TestCase):

    def test_place_mark(self):
        with self.assertRaises(IndexError):
            grid[-1][1] = 'X' # Invalid row

        with self.assertRaises(IndexError): 
            grid[1][3] = 'X' # Invalid col

    def test_check_winner(self):
        grid[0][0] = 'X'
        grid[1][1] = 'X' 
        grid[2][2] = 'X'
        self.assertEqual(winner, 'X')
        
        reset_game()
        
        grid[0][0] = 'O'
        grid[0][1] = 'O' 
        grid[0][2] = 'O'
        self.assertEqual(winner, 'O')

    def test_check_tie(self):
        # Fill grid with X's and O's
        grid[0][0] = 'X'
        ...

        self.assertTrue(tie)

        self.assertEqual(grid, ['','',''],['','',''], ['','',''])
        self.assertEqual(current_player, 'X')
        self.assertFalse(tie)
        
if __name__ == '__main__':
    unittest.main()