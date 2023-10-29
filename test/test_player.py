import unittest
from unittest.mock import patch, Mock
from io import StringIO
from ..game.player import Player

class TestPlayer(unittest.TestCase):

    @patch('builtins.open', side_effect=[StringIO("WORD\nXYZ\n"), open("scrabble-2023-abenavidezUM/dic.txt", "r")])
    def test_player_initialization(self, mock_open):
        # Verifica la inicialización de la clase Player
        tile_bag_mock = Mock()
        player = Player("Alice", tile_bag_mock)
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.score, 0)
        self.assertEqual(len(player.rack), 7)
        self.assertEqual(player.tile_bag, tile_bag_mock)

    @patch('builtins.open', side_effect=[StringIO("WORD\nXYZ\n"), open("scrabble-2023-abenavidezUM/dic.txt", "r")])
    def test_fill_rack(self, mock_open):
        # Verifica que el método fill_rack llena el rack hasta 7 fichas
        tile_bag_mock = Mock()
        tile_bag_mock.take_tile.side_effect = ["A", "B", "C", "D", "E"]
        player = Player("Alice", tile_bag_mock)
        self.assertEqual(len(player.rack), 7)

    @patch('builtins.open', side_effect=[StringIO("WORD\nXYZ\n"), open("scrabble-2023-abenavidezUM/dic.txt", "r")])
    def test_play_word(self, mock_open):
        # Verifica el juego de palabras en Player
        tile_bag_mock = Mock()
        player = Player("Alice", tile_bag_mock)
        player.rack = ["W", "O", "R", "D", " ", " ", " "]
        initial_score = player.score

        board_mock = Mock()
        board_mock.is_valid_move.return_value = True
        board_mock.calculate_word_score.return_value = 10

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            player.play_word("WORD", 0, 0, "right", board_mock)
            game_output = mock_stdout.getvalue()
            self.assertNotEqual(player.score, initial_score)  # La puntuación del jugador debe aumentar

    @patch('builtins.open', side_effect=[StringIO("WORD\nXYZ\n"), open("scrabble-2023-abenavidezUM/dic.txt", "r")])
    def test_play_word_invalid_direction(self, mock_open):
        # Verifica que Player maneje una dirección de palabra no válida
        tile_bag_mock = Mock()
        player = Player("Alice", tile_bag_mock)
        player.rack = ["W", "O", "R", "D", " ", " ", " "]
        initial_score = player.score

        board_mock = Mock()
        board_mock.is_valid_move.return_value = True
        board_mock.calculate_word_score.return_value = 10

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            player.play_word("WORD", 0, 0, "invalid", board_mock)
            game_output = mock_stdout.getvalue()
            self.assertIn("Invalid direction.", game_output)  # Se debe mostrar un mensaje de dirección inválida
            self.assertEqual(player.score, initial_score)  # La puntuación del jugador no debe cambiar

    @patch('builtins.open', side_effect=[StringIO("WORD\nXYZ\n"), open("scrabble-2023-abenavidezUM/dic.txt", "r")])
    def test_play_word_invalid_word(self, mock_open):
        # Verifica que Player maneje una palabra no válida
        tile_bag_mock = Mock()
        player = Player("Alice", tile_bag_mock)
        player.rack = ["W", "O", "R", "D", " ", " ", " "]
        initial_score = player.score

        board_mock = Mock()
        board_mock.is_valid_move.return_value = True
        board_mock.calculate_word_score.return_value = 10

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            player.play_word("XYZ", 0, 0, "right", board_mock)
            game_output = mock_stdout.getvalue()
            self.assertIn("Invalid word.", game_output)  # Se debe mostrar un mensaje de palabra inválida
            self.assertEqual(player.score, initial_score)  # La puntuación del jugador no debe cambiar

if __name__ == '__main__':
    unittest.main()
