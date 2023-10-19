import unittest
from unittest.mock import MagicMock
from test_models import Player, TileBag

class TestPlayer(unittest.TestCase):

    def setUp(self):
        #Configurar datos de prueba
        word_list = ["WORD", "SCRABBLE", "PYTHON", "TEST"]
        tile_bag = TileBag(word_list)
        self.player = Player("Alice", tile_bag)

    def test_fill_rack(self):
        #Verificar que el método fill_rack llene la rack del jugador con letras
        self.assertEqual(len(self.player.rack), 7)

    def test_play_word_valid(self):
        #Verificar que el método play_word coloque una palabra válida en el tablero y actualice la puntuación
        self.player.rack = ["W", "O", "R", "D", " ", " ", " "]

        #Creamos un objeto Mock para simular el tablero (MockBoard)
        mock_board = MagicMock()

        #Configuramos el comportamiento esperado del objeto Mock para place_word
        mock_board.place_word.return_value = True  # Suponemos que la palabra se puede colocar en el tablero
        mock_board.calculate_word_score.return_value = 4  # Suponemos que la palabra "WORD" vale 4 puntos

        self.player.play_word("WORD", 0, 0, "right", mock_board)
        
        #Asegurarse de que el método place_word se llamó con los argumentos correctos
        mock_board.place_word.assert_called_with("WORD", 0, 0, "right")

        #Asegurarse de que la puntuación del jugador se actualice correctamente
        self.assertEqual(self.player.score, 4)

    def test_play_word_invalid_direction(self):
        #Verificar que el método play_word maneje una dirección de palabra no válida
        mock_board = MagicMock()
        self.player.play_word("WORD", 0, 0, "invalid", mock_board)

        #Asegurarse de que la puntuación del jugador no se haya actualizado
        self.assertEqual(self.player.score, 0)

    def test_play_word_invalid_word(self):
        #Verificar que el método play_word maneje una palabra no válida
        mock_board = MagicMock()
        self.player.rack = ["X", "Y", "Z", " ", " ", " ", " "]
        self.player.play_word("XYZ", 0, 0, "right", mock_board)

        #Asegurarse de que la puntuación del jugador no se haya actualizado
        self.assertEqual(self.player.score, 0)

    def test_exchange_tiles(self):
        #Verificar que el método exchange_tiles intercambie correctamente las fichas
        self.player.rack = ["A", "B", "C", "D", "E", "F", "G"]
        initial_rack = self.player.rack.copy()
        tiles_to_exchange = ["A", "C", "E"]

        #Creamos un objeto Mock para simular el TileBag
        mock_tile_bag = MagicMock()
        mock_tile_bag.exchange_tiles.return_value = ["X", "Y", "Z"]

        self.player.tile_bag = mock_tile_bag
        self.player.exchange_tiles(tiles_to_exchange)

        #Verificar que el método exchange_tiles del TileBag se llamó con los argumentos correctos
        mock_tile_bag.exchange_tiles.assert_called_with(tiles_to_exchange)

        #Verificar que las fichas intercambiadas ya no estén en la rack y que se hayan agregado nuevas
        for tile in tiles_to_exchange:
            self.assertNotIn(tile, self.player.rack)
        self.assertEqual(len(self.player.rack), len(initial_rack) - len(tiles_to_exchange) + 3)

if __name__ == '__main__':
    unittest.main()

