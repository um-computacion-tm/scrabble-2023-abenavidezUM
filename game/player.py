class Player:
    def __init__(self, name, tile_bag):
        self.name = name
        self.rack = []
        self.score = 0

        # Cargar el diccionario de palabras desde el archivo "scrabble-2023-abenavidezUM/game/dic.txt"
        with open("scrabble-2023-abenavidezUM/dic.txt", "r") as file:
            dictionary = [line.strip() for line in file]

        # Inicializar el TileBag con el diccionario cargado
        self.tile_bag = tile_bag
        self.tile_bag.dictionary = dictionary

        self.fill_rack()

    def fill_rack(self):
        while len(self.rack) < 7 and self.tile_bag.tiles:
            self.rack.append(self.tile_bag.take_tile())

    def play_word(self, word, row, col, direction, board):
        if direction not in ("right", "down"):
            print("Invalid direction. Please enter 'right' or 'down'.")
            return

        if not self.is_valid_word(word):
            print("Invalid word. Please enter a valid word.")
            return

        if not board.is_valid_move(word, row, col, direction):
            print("Invalid move. Please check your coordinates and direction.")
            return

        # Place the word on the board
        board.place_word(word, row, col, direction)
        
        # Calculate the word score and update the player's score
        word_score = board.calculate_word_score(word, row, col, direction)
        self.score += word_score

        # Remove the used tiles from the player's rack
        for letter in word:
            self.rack.remove(letter)

    def exchange_tiles(self, tiles_to_exchange):
        if not all(tile in self.rack for tile in tiles_to_exchange):
            print("Invalid tiles to exchange. Make sure you have these tiles in your rack.")
            return

        # Exchange the tiles with the TileBag
        new_tiles = self.tile_bag.exchange_tiles(tiles_to_exchange)
        
        # Remove the exchanged tiles from the player's rack
        for tile in tiles_to_exchange:
            self.rack.remove(tile)
        
        # Fill the player's rack with new tiles
        self.rack.extend(new_tiles)

    def is_valid_word(self, word):
        return word in self.tile_bag.dictionary

    def __str__(self):
        return f"{self.name} (Score: {self.score})"
