import unittest
from game.models import (
    TileBag,
    Tile,
)
from unittest.mock import patch


class TestTile(unittest.TestCase):
    def test_tile_creation(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.get_letter(), 'A')
        self.assertEqual(tile.get_value(), 1)


if __name__ == '__main__':
    unittest.main()
