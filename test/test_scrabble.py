import unittest
from unittest.mock import patch, Mock
from io import StringIO
from test_scrabble import ScrabbleGame, ScrabbleCli

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
    
    @patch('builtins.input', side_effect=["WORD", "0", "0", "right", " "])
    def test_scrabble_game_play_word(self, mock_input):
        # Verifica el juego de palabras en ScrabbleGame
        game = ScrabbleGame(["Alice"])
        player = game.players[0]
        player.rack = ["W", "O", "R", "D", " ", " ", " "]
        initial_score = player.score

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            game.start_game()
            game_output = mock_stdout.getvalue()
            self.assertIn("Round 2:", game_output)  # El número de ronda debe aumentar
            self.assertNotEqual(player.score, initial_score)  # La puntuación del jugador debe aumentar

    @patch('builtins.input', side_effect=["WORD", "0", "0", "invalid", " "])
    def test_scrabble_game_play_word_invalid_direction(self, mock_input):
        # Verifica que ScrabbleGame maneje una dirección de palabra no válida
        game = ScrabbleGame(["Alice"])
        player = game.players[0]
        player.rack = ["W", "O", "R", "D", " ", " ", " "]
        initial_score = player.score

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            game.start_game()
            game_output = mock_stdout.getvalue()
            self.assertIn("Invalid direction.", game_output)  # Se debe mostrar un mensaje de dirección inválida
            self.assertEqual(player.score, initial_score)  # La puntuación del jugador no debe cambiar

    @patch('builtins.input', side_effect=["XYZ", "0", "0", "right", " "])
    def test_scrabble_game_play_word_invalid_word(self, mock_input):
        # Verifica que ScrabbleGame maneje una palabra no válida
        game = ScrabbleGame(["Alice"])
        player = game.players[0]
        player.rack = ["W", "O", "R", "D", " ", " ", " "]
        initial_score = player.score

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            game.start_game()
            game_output = mock_stdout.getvalue()
            self.assertIn("Invalid word.", game_output)  # Se debe mostrar un mensaje de palabra inválida
            self.assertEqual(player.score, initial_score)  # La puntuación del jugador no debe cambiar



if __name__ == '__main__':
    unittest.main()