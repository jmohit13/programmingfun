#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = sorted(ranked, reverse=True)
    num_players = len(ranked)
    num_games = len(player)

    # rank the existing leaderboard
    rl = [(1,ranked[i]) for i in range(0,len(ranked))]

    for i in range(0,len(ranked)):
        for j in range(i+1, len(ranked)):
            if ranked[i] != ranked[j]:
                rl[j] = (rl[i][0]+1, ranked[j])
            else:
                rl[j] = (rl[i][0], ranked[j])
            break;

    player_rank_list = []
    for score in player:
        for i in range(0,len(rl),1):
            if score < rl[i][1]:
                player_rank = rl[i][0]+1
            if score == rl[i][1]:
                player_rank = rl[i][0]
            if 1 == rl[i][0] and score > rl[i][1]:
                player_rank = rl[i][0]
        player_rank_list.append(player_rank)

    return player_rank_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
