#Clases ScrabbleGame y ScrabbleCli
#Actualizar test

from random import shuffle
from models import TileBag
from dictionary import Dictionary
from board import Board
from player import Player

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
