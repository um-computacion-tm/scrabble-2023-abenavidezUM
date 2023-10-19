# Clases Tile y TileBag

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
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
            'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
            'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
            'Y': 4, 'Z': 10
        }
        for letter, value in letter_values.items():
            self.add_to_bag(Tile(letter, value))
        shuffle(self.tiles)

    def add_to_bag(self, tile):
        self.tiles.append(tile)

    def take_tile(self):
        if self.tiles:
            return self.tiles.pop()
        else:
            print("The tile bag is empty.")
            return None

    def exchange_tiles(self, tiles_to_exchange):
        for tile in tiles_to_exchange:
            if tile in self.tiles:
                self.tiles.remove(tile)
        
        # Agrega las fichas intercambiadas de nuevo a la bolsa
        self.tiles.extend(tiles_to_exchange)