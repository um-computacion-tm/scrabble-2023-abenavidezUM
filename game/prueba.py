from random import shuffle

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def get_letter(self):
        return self.letter

    def get_value(self):
        return self.value

class TileBag:
    def __init__(self):
        self.tiles = []
        self.initialize_tiles()

    def initialize_tiles(self):
        # Llenar la bolsa con fichas y barajar
        pass

    def take_tile(self):
        # Tomar una ficha de la bolsa
        pass

    def exchange_tiles(self, tiles_to_exchange):
        # Intercambiar fichas del jugador con la bolsa
        pass

class Dictionary:
    def __init__(self, word_list):
        self.word_list = word_list

    def is_valid_word(self, word):
        # Verificar si una palabra es válida en el diccionario
        pass

class Board:
    def __init__(self):
        self.board = []

    def place_word(self, word, row, col, direction):
        # Colocar una palabra en el tablero
        pass

    def calculate_score(self, word, row, col, direction):
        # Calcular la puntuación de una palabra en el tablero
        pass

class Player:
    def __init__(self, name, tile_bag):
        self.name = name
        self.rack = []
        self.score = 0
        self.tile_bag = tile_bag
        self.fill_rack()

    def fill_rack(self):
        # Llenar el rack del jugador con fichas
        pass

    def play_word(self, word, row, col, direction, board):
        # Jugar una palabra en el tablero
        pass

    def exchange_tiles(self, tiles_to_exchange):
        # Intercambiar fichas con la bolsa
        pass

class ScrabbleGame:
    def __init__(self, player_names):
        self.tile_bag = TileBag()
        self.dictionary = Dictionary(load_dictionary())
        self.board = Board()
        self.players = [Player(name, self.tile_bag) for name in player_names]
        self.current_player_index = 0
        self.round_number = 1

    def start_game(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            # Lógica para controlar el turno del jugador actual
            # Solicitar palabra, posición, dirección, intercambio, etc.
            self.board.place_word(word, row, col, direction)
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            self.round_number += 1

    def is_game_over(self):
        # Lógica para verificar si el juego ha terminado
        pass

class ScrabbleCli:
    def __init__(self):
        self.game = None

    def run(self):
        # Lógica para ejecutar el juego en la línea de comando
        pass

if __name__ == "__main__":
    cli = ScrabbleCli()
    cli.run()
