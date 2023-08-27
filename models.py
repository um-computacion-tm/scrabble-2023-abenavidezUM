#Clases Tile y TileBag
#Actualizar test
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