import unittest
from game.board import Board

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
        
        
if __name__ == '__main__':
    unittest.main()