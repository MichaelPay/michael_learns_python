#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:12:59 2017

@author: root
"""
# pip install coverage
# coverage run test.py
# coverage report
# coverage report -m
# OUTPUT:
# Name      Stmts   Miss  Cover   Missing
# ---------------------------------------
# dice.py      51     13    75%   21-22, 34, 55-56, 68, 71, 74, 77, 80-83
# test.py      26      0   100%
# ---------------------------------------
# TOTAL        77     13    83%


import unittest

import dice

class DieTest(unittest.TestCase):
    def setUp(self):
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)

    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d6.value, range(1, 7))

    def test_add(self):
        self.assertIsInstance(self.d6 + self.d8, int)

class RollTests(unittest.TestCase):
    def setUp(self):
        self.hand1 = dice.Roll('1d2')
        self.hand3 = dice.Roll('3d6')

    def test_lower(self):
        self.assertGreaterEqual(int(self.hand3),3)

    def test_upper(self):
        self.assertLessEqual(int(self.hand3), 18)

    def test_membership(self):
        test_die = dice.Die(2)
        test_die.value = self.hand1.results[0].value
        self.assertIn(test_die,self.hand1.results)


if __name__ == '__main__':
    unittest.main()