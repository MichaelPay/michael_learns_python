# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:21:11 2017

@author: Monic
"""

class YatzyScoresheet:
    
    def score_ones(self, hand):
        return sum(hand.ones)
    
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)