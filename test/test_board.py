import unittest
from ..game.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        # Configurar una instancia de la clase Board para las pruebas
        self.board = Board()

    def test_initial_board(self):
        # Verificar que el tablero se inicializa correctamente
        self.assertEqual(len(self.board.get_board()), 15)  # El tablero debe tener 15 filas
        self.assertEqual(len(self.board.get_board()[0]), 15)  # Cada fila debe tener 15 columnas

    def test_place_word(self):
        # Verificar que se pueda colocar una palabra en el tablero
        word = "HELLO"
        row, col = 7, 7  # Coordenadas donde se coloca la primera letra
        direction = "right"
        self.assertTrue(self.board.is_valid_placement(word, row, col, direction))
        self.board.place_word(word, row, col, direction)

        # Verificar que las letras se colocaron correctamente en el tablero
        self.assertEqual(self.board.get_square(7, 7), "H")
        self.assertEqual(self.board.get_square(7, 8), "E")
        self.assertEqual(self.board.get_square(7, 9), "L")
        self.assertEqual(self.board.get_square(7, 10), "L")
        self.assertEqual(self.board.get_square(7, 11), "O")

    def test_place_word_invalid(self):
        # Verificar que no se pueda colocar una palabra en una ubicación inválida
        word = "INVALID"
        row, col = 13, 13  # Coordenadas fuera del tablero
        direction = "right"
        self.assertFalse(self.board.is_valid_placement(word, row, col, direction))

        row, col = 7, 7  # Intentar colocar en una ubicación ya ocupada
        self.assertTrue(self.board.is_valid_placement("HELLO", row, col, direction))
        self.board.place_word("HELLO", row, col, direction)
        self.assertFalse(self.board.is_valid_placement(word, row, col, direction))

    def test_is_valid_move_right(self):
        # Agrega pruebas para is_valid_move con palabras válidas y no válidas en dirección "right"
        self.assertTrue(self.board.is_valid_placement("HELLO", 7, 7, "right"))
        self.assertFalse(self.board.is_valid_placement("WORLD", 14, 10, "right"))  # Invalid placement

    def test_is_valid_move_down(self):
        # Agrega pruebas para is_valid_move con palabras válidas y no válidas en dirección "down"
        self.assertTrue(self.board.is_valid_placement("PYTHON", 6, 5, "down"))
        self.assertFalse(self.board.is_valid_placement("TESTING", 12, 2, "down"))  # Invalid placement

if __name__ == '__main__':
    unittest.main()
