#Clases ScrabbleGame y ScrabbleCli
#Actualizar test

from random import shuffle
from models import TileBag
from dictionary import Dictionary
from board import Board
from player import Player

class ScrabbleGame:
    def __init__(self, player_names):
        with open("dic.txt", "r") as file:
            word_list = [line.strip() for line in file]

        self.dictionary = Dictionary(word_list)
        self.tile_bag = TileBag()
        self.board = Board()
        self.players = [Player(name, self.tile_bag) for name in player_names]
        self.current_player_index = 0
        self.round_number = 1

    def start_game(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            print("\nRound {}: {}'s turn".format(self.round_number, current_player.name))
            print(self.board.get_board())
            print("{}'s Letter Rack: {}".format(current_player.name, ", ".join(tile.get_letter() for tile in current_player.rack)))

            word = input("Enter a word to play (or leave empty to exchange tiles): ")
            if not word:
                tiles_to_exchange = input("Enter tiles to exchange (separated by spaces): ").split()
                current_player.exchange_tiles(tiles_to_exchange)
            else:
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                direction = input("Enter direction (right or down): ")
                current_player.play_word(word, row, col, direction, self.board)
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
                self.round_number += 1

    def is_game_over(self):
        return all(len(player.rack) == 0 and len(self.tile_bag.tiles) == 0 for player in self.players)

class ScrabbleCli:
    def __init__(self):
        self.game = None

    def run(self):
        print("Scrabble Game")
        num_players = int(input("Enter the number of players (2-4): "))
        player_names = [input("Enter player {}'s name: ".format(i + 1)) for i in range(num_players)]
        self.game = ScrabbleGame(player_names)
        self.game.start_game()

if __name__ == "__main__":
    game_cli = ScrabbleCli()
    game_cli.run()