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
    p0_results_array = np.zeros((3,27), dtype=int)

    for i in range(number):
        g = Game()
        firstmove = g.single_move(0)
        winner = g.play_game(next_player=1)

        if winner == 0:
            p0_results_array[0, firstmove] += 1
        elif winner == 4:
            p0_results_array[2, firstmove] += 1
        else:
            p0_results_array[1, firstmove] += 1

    return p0_results_array

results_matrix = p0_start_game_results(100000)
print(results_matrix)
    #return start_index, p0_aggregate
    #print(p0_results)

#firstmove, outcome = p0_start_game_results(10)
#print(firstmove, outcome)



#str_game_res, run_time, int_game_res = record_game_results(10000)

#headers = ['p0', 'p1', 'p2', 'p3', 'ties']
#with open('Otrio_Stats_TEST.csv', 'w') as f:
    #f.write(','.join(headers))
    #f.write('\n')
    #f.write(','.join(str_game_res))
    #f.close()

#print(int_game_res, float(run_time))


