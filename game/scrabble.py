#Clases ScrabbleGame y ScrabbleCli
#Actualizar test

from random import shuffle
from models import TileBag
from dictionary import Dictionary
from board import Board
from player import Player

class ScrabbleGame:
    def __init__(self, player_names):
        try:
            with open("dic.txt", "r") as file:
                word_list = [line.strip() for line in file]
        except FileNotFoundError:
            print("Error: El archivo de palabras 'dic.txt' no se encontró. Asegúrate de que el archivo exista.")
            exit(1)

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

        # Juego terminado, determina al ganador o si hay un empate
        max_score = max(player.score for player in self.players)
        winners = [player for player in self.players if player.score == max_score]

        if len(winners) == 1:
            print(f"{winners[0].name} wins with a score of {winners[0].score}!")
        else:
            print("It's a tie! The game is over.")

    def is_game_over(self):
        return all(len(player.rack) == 0 and len(self.tile_bag.tiles) == 0 for player in self.players)

class ScrabbleCli:
    def __init(self):
        self.game = None

    def run(self):
        print("Scrabble Game")
        num_players = int(input("Enter the number of players (2-4): "))

        if num_players < 2 or num_players > 4:
            print("Invalid number of players. Please enter 2-4 players.")
            return

        player_names = []
        for i in range(num_players):
            name = input(f"Enter player {i + 1}'s name: ")
            if name in player_names:
                print("Player names must be unique. Please choose a different name.")
                return
            player_names.append(name)

        self.game = ScrabbleGame(player_names)
        self.game.start_game()

if __name__ == "__main__":
    game_cli = ScrabbleCli()
    game_cli.run()
