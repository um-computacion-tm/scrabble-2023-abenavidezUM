import unittest
from ..game.models import (
    TileBag,
    Tile,
)
from unittest.mock import patch


class TestTile(unittest.TestCase):
    def test_tile_creation(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.get_letter(), 'A')
        self.assertEqual(tile.get_value(), 1)

class TestTileBag(unittest.TestCase):
    def setUp(self):
        # Set up a token bag with some tokens for tests
        self.tile_bag = TileBag()
        self.tile_bag.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

    def test_initialize_tiles(self):
        # Check if the bag is initialized correctly
        self.tile_bag.initialize_tiles()
        self.assertEqual(len(self.tile_bag.tiles), 98)  

    def test_take_tile(self):
        # Check if a chip is taken from the bag
        tile = self.tile_bag.take_tile()
        self.assertEqual(tile.get_value(), 3)  

    def test_exchange_tiles(self):
        # Verify the exchange of tokens in the stock exchange
        tiles_to_exchange = [Tile('B', 3)]
        new_tiles = self.tile_bag.exchange_tiles(tiles_to_exchange)
        self.assertEqual(len(new_tiles), 1)  
        self.assertEqual(len(self.tile_bag.tiles), 2)  

if __name__ == '__main__':
    unittest.main()
