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
    result_count = {'p0_wins': 0,
                    'p1_wins': 0,
                    'p2_wins': 0,
                    'p3_wins': 0,
                    'ties': 0}
    #result_count = [0] * 5
    result = []
    k = result_count.keys()

    for i in range(number):
        g = Game()
        result.append(g.play_game())

    for r in result:
        if r == 0:
            result_count['p0_wins'] += 1
        elif r == 1:
            result_count['p1_wins'] += 1
        elif r == 2:
            result_count['p2_wins'] += 1
        elif r == 3:
            result_count['p3_wins'] += 1
        else:
            result_count['ties'] += 1


    end_time = time.time()
    run_time = end_time - start_time
    return result_count, run_time

game_results, run_time = record_game_results(10000)
print(game_results, float(run_time))

