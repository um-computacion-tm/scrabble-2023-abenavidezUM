#Clases Board
#Actualizar test


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.premium_squares = self.create_premium_squares()

    def create_premium_squares(self):
        # Define los cuadrados premium en el tablero.
        premium_squares = [
            (0, 0), (0, 7), (0, 14),
            (7, 0), (7, 7), (7, 14),
            (14, 0), (14, 7), (14, 14)
        ]
        return premium_squares

    def place_word(self, word, row, col, direction):
        word = word.upper()
        word_length = len(word)
        
        if direction == 'right':
            for i in range(word_length):
                self.board[row][col + i] = word[i]
        elif direction == 'down':
            for i in range(word_length):
                self.board[row + i][col] = word[i]

    def is_valid_placement(self, word, row, col, direction):
        word = word.upper()
        word_length = len(word)
        
        if direction == 'right':
            if col + word_length > 15:
                return False
            for i in range(word_length):
                if self.board[row][col + i] != ' ' and self.board[row][col + i] != word[i]:
                    return False
        elif direction == 'down':
            if row + word_length > 15:
                return False
            for i in range(word_length):
                if self.board[row + i][col] != ' ' and self.board[row + i][col] != word[i]:
                    return False
        return True

    def get_board(self):
        return self.board

    def get_square(self, row, col):
        return self.board[row][col]

    def get_premium_squares(self):
        return self.premium_squares
