"""Can also be used in the terminal with
python -m unittest test.py
Under the correct directory
"""

import unittest

import moves


class MoveTest(unittest.TestCase):
    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_five_times_five(self):
        assert 5 * 5 == 25

    def test_one_plus_one(self):
        assert 1 + 1 == 2

    def test_five_times_six(self):
        assert 5 * 6 == 30

    def test_five_plus_6(self):
        assert 5 + 6 == 11


"""moves.Rock() calls upon the Rock method from the moves class"""


class MoveTest2(unittest.TestCase):
    def test_equal(self):
        rock1 = moves.Rock()
        rock2 = moves.Rock()
        self.assertEqual(rock1, rock2)

    def test_not_equal(self):
        rock = moves.Rock()
        paper = moves.Paper()
        self.assertNotEqual(rock, paper)


"""Setting up the test for code simplification,
The following code is the same as MoveTest2 class"""


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()

    def test_equal(self):
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        self.assertNotEqual(self.rock, self.paper)

    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock,self.scissors)

    def test_paper_worse_than_scissors(self):
        self.assertLess(self.paper,self.scissors)


if __name__ == '__main__':
    unittest.main()
