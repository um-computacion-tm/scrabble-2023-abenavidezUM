class Cell:
    def __init__(self, letter_multiplier=1, word_multiplier=1):
        self.tile = None  
        self.letter_multiplier = letter_multiplier 
        self.word_multiplier = word_multiplier  

    def place_tile(self, tile):
        """Coloca una ficha en la celda"""
        self.tile = tile

    def remove_tile(self):
        """Quita la ficha de la celda"""
        self.tile = None

    def is_empty(self):
        """Verifica si la celda está vacía"""
        return self.tile is None

    def get_score(self):
        """Calcula la puntuacion total de la celda. Considera multiplicadores"""
        if self.is_empty():
            return 0
        tile_value = self.tile.get_value()
        score = tile_value * self.letter_multiplier
        return score * self.word_multiplier
