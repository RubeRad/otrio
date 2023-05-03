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
    str_result_count = [0] * 5
    result = []

    for i in range(number):
        g = Game()
        result.append(g.play_game())

    for r in result:
        result_count[r] += 1

    for i in range(len(result_count)):
        str_result_count[i] = (str(result_count[i]))

    end_time = time.time()
    run_time = end_time - start_time
    return str_result_count, run_time, result_count

def p0_start_game_results(number):
    start_time = time.time()
    result_count = [0] * 5
    str_result_count = [0] * 5
    p0_win = 0
    p0_loss = 0
    p0_tie = 0
    start_index = []

    for i in range(number):
        g = Game()
        firstmove = g.single_move(0)
        start_index.append(firstmove)
        winner = g.play_game(next_player=1)

        if winner == 0:
            p0_win += 1
        elif winner == 4:
            p0_tie += 1
        else:
            p0_loss += 1

    p0_results = list(str(p0_win))
    p0_results.append(str(p0_loss))
    p0_results.append(str(p0_tie))

    return start_index, p0_results
    #print(p0_results)

firstmove, outcome = p0_start_game_results(10)
print(firstmove, outcome)



#str_game_res, run_time, int_game_res = record_game_results(10000)

#headers = ['p0', 'p1', 'p2', 'p3', 'ties']
#with open('Otrio_Stats_TEST.csv', 'w') as f:
    #f.write(','.join(headers))
    #f.write('\n')
    #f.write(','.join(str_game_res))
    #f.close()

#print(int_game_res, float(run_time))


