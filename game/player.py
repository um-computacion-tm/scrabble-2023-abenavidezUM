#Clases Player
#Actualizar test

class Player:
    def __init__(self, name, tile_bag):
        self.name = name
        self.rack = []
        self.score = 0
        self.tile_bag = tile_bag
        self.fill_rack()

    def fill_rack(self):
        while len(self.rack) < 7 and self.tile_bag.tiles:
            self.rack.append(self.tile_bag.take_tile())

    def play_word(self, word, row, col, direction, board):
        # Jugar una palabra en el tablero
        pass

    def exchange_tiles(self, tiles_to_exchange):
        new_tiles = self.tile_bag.exchange_tiles(tiles_to_exchange)
        self.rack.extend(new_tiles)
    
    