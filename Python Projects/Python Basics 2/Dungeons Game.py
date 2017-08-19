# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 22:18:17 2017

@author: Monic
"""

import random
import os
CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),
         (0,1),(1,1),(2,1),(3,1),(4,1),
         (0,2),(1,2),(2,2),(3,2),(4,2),
         (0,3),(1,3),(2,3),(3,3),(4,3),
         (0,4),(1,4),(2,4),(3,4),(4,4),
        
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# draw grid
# draw player in the world
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

def get_locations():
    monster, door, player = random.sample(CELLS,3)
    
    return monster, door, player


    
    # Good move? change the player's position
    # Bad move? don't change anything
    # On the door? They win!
    # On the monster? They lose
    # Otherwise, Loop back around

def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x+=1
    if move == 'UP':
        y-=1
    if move == 'DOWN':
        y+=1
    return x,y

def get_moves(player):
    moves = ["LEFT", "UP","RIGHT","DOWN"]
    x , y = player
    if x == 0:
        moves.remove('LEFT')
    elif x == 4:
        moves.remove('RIGHT')
    elif y == 0:
        moves.remove('UP')
    elif y == 4:
        moves.remove('DOWN')
    return moves
def draw_map(player):
    print(' _'*5)
    tile = '|{}'
    
def game_loop():
    monster, door, player = get_locations()
    while True:
        draw_map(player)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player)) #fill with player position
        print("You can move {}".format(', '.join(valid_moves))) #fill with available moves
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            break
        if move in valid_moves:
            player = move_player(player, move)
        else:
            input("you can't move into a wall!!! hahahhaha")
        clear_screen()

clear_screen()
print("Welcome to the dungeon!")
print('Press start to begin game')
clear_screen()
game_loop()




