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
        letter_values = {
            #Valores de las letras
        }
        for letter, value in letter_values.items():
            self.add_to_bag(Tile(letter, value), 1)
        shuffle(self.tiles)

    def add_to_bag(self, tile, quantity):
        self.tiles.extend([tile] * quantity)

    def take_tile(self):
        return self.tiles.pop()

    def exchange_tiles(self, tiles_to_exchange):
        for tile in tiles_to_exchange:
            self.tiles.remove(tile)
        self.initialize_tiles()
        return [self.take_tile() for _ in range(len(tiles_to_exchange))]