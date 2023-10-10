import unittest
from unittest.mock import patch, Mock
from io import StringIO
from scrabble import ScrabbleGame, ScrabbleCli

class TestScrabbleGame(unittest.TestCase):

    @patch('builtins.input', side_effect=["Alice", "Bob"])
    def test_scrabble_game_initialization(self, mock_input):
        # Verifica la inicialización de ScrabbleGame
        game = ScrabbleGame(["Alice", "Bob"])
        self.assertEqual(game.current_player_index, 0)
        self.assertEqual(game.round_number, 1)
        self.assertEqual(len(game.players), 2)

    @patch('builtins.input', return_value=" ")
    def test_scrabble_game_exchange_tiles(self, mock_input):
        # Verifica el intercambio de fichas en ScrabbleGame
        game = ScrabbleGame(["Alice"])
        player = game.players[0]
        initial_rack = player.rack.copy()
        game.tile_bag.tiles = ['A', 'B', 'C', 'D', 'E']

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value="A B C"):
                game.start_game()
                exchanged_tiles = mock_stdout.getvalue().strip().split()
                self.assertEqual(len(exchanged_tiles), 3)
                self.assertNotIn("A", player.rack)
                self.assertNotIn("B", player.rack)
                self.assertNotIn("C", player.rack)
                self.assertEqual(len(player.rack), len(initial_rack) - 3 + len(exchanged_tiles))


if __name__ == '__main__':
    unittest.main()