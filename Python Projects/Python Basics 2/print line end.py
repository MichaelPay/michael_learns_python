# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:58:08 2017

@author: Monic
"""

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for x in TILES:
    if x = '||':
        line_end = '\n'
        print(x, end = line_end)
    else:
        line_end = ''
        print(x, end = line_end)