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

def p0_start_whole_game_results(number, file):
    p0_results_array = np.zeros((3,27), dtype=int)
    with open(file, 'w') as f:
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

            f.write(str(winner) + ',' + ','.join(g.move_tracker) + '\n')

    return p0_results_array

#results_matrix = p0_start_game_results(1000)
#print(results_matrix)
#print(sum(results_matrix[0,]))
#print(results_matrix[0,13])

#mid_mid = results_matrix[0,13] / sum(results_matrix[0,])
#mid_mid_p = mid_mid * 100
#print(mid_mid_p)
    #return start_index, p0_a / ggregate
    #print(p0_results)

mil_games_outcome = p0_start_whole_game_results(1000000,'Otrio_Dataset.csv')
with open('Otrio_Dataset_Matrix.csv', 'w') as f:
    print(mil_games_outcome, file=f)




#str_game_res, run_time, int_game_res = record_game_results(10000)

#headers = ['p0', 'p1', 'p2', 'p3', 'ties']
#with open('Otrio_Stats_TEST.csv', 'w') as f:
    #f.write(','.join(headers))
    #f.write('\n')
    #f.write(','.join(str_game_res))
    #f.close()

#print(int_game_res, float(run_time))


