import unittest
from Algorithm.boyer_moore import search


class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search("", "a"), 0)
        self.assertEqual(search("abcabcaaaaaaaaa", "abc"), 2)
        self.assertEqual(search("The dog ran for the ball!", "dog"), 1)
        self.assertEqual(search("Hi Hi Hi Hi Hi Hi Hi HiHiHiHi", "Hi"), 11)
