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
        # Llenar el rack del jugador con fichas
        pass

    def play_word(self, word, row, col, direction, board):
        # Jugar una palabra en el tablero
        pass

    def exchange_tiles(self, tiles_to_exchange):
        # Intercambiar fichas con la bolsa
        pass
    
    