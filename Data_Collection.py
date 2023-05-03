import numpy as np
import random
import time
import csv

from OtrioArtist import *
from Player import *
from Game import *

#This script is to collect information from an arbitrary number of games (2.7m???).

#Data includes:
    #Total number of games won/tied
    #Count of wins/ties for each player as a starting player
    #Count of wins/ties for each starting position (0-26) ???
    #Images of final game states (and one move before???)

#File formats include: .csv, .png

def record_game_results(number):
    start_time = time.time()
    result_count = [0] * 5
    result = []

    for i in range(number):
        g = Game()
        result.append(g.play_game())

    for r in result:
        result_count[r] += 1

    end_time = time.time()
    run_time = end_time - start_time
    return result_count, run_time

game_results, run_time = record_game_results(100)

'''
headers = ['p0', 'p1', 'p2', 'p3', 'ties']
with open('Otrio_Stats_TEST.csv', 'w') as f:
    for item in headers:
        str_val_h = headers[item].join(',')
    for item in game_results:
        str_val_d = game_results[item].join(',')

    f.write(str_val_h)
    f.write(str_val_d)
    f.close()
'''
print(game_results, float(run_time))

