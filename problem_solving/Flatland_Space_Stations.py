#!/bin/python3

import math
import os
import random
import re
import sys

# todo time complexity

def find_nearest_stations(input_station, stations):
    dl = [abs(input_station - i) for i in stations]
    return dl.index(min(dl))

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):

    sorted_list = sorted(c)
    station_distances = [abs(i - sorted_list[find_nearest_stations(i, sorted_list)]) for i in range(n)]

    # for i in range(n):
    #     near_station_index = find_nearest_stations(i, sorted_list)
    #     dist_to_station = abs(i - sorted_list[near_station_index])
    #     station_distances.append(dist_to_station)
    #     # print(i, sorted_list[near_station_index])

    return max(station_distances)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
