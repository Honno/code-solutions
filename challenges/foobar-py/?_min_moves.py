#!/usr/bin/env python2

from collections import defaultdict, deque
from itertools import product
from operator import add

def vectorsum(*vectors):
    if len(vectors) > 1:
        return map(add, vectors[0], vectorsum(*vectors[1:]))
    else:
        return vectors[0]

def gen_knight_moves():
    up, right, down, left = (-1, 0), (0, 1), (1, 0), (0, -1)
    for x, y in product([left, right], [up, down]):
        yield(vectorsum(x,x,y))
        yield(vectorsum(y,y,x))

KNIGHT_VECTORS = list(gen_knight_moves())
BOARD = [list(range(x*8, x*8+8)) for x in range(8)]

def get_coords(pos):
    for y, row in enumerate(BOARD):
        for x, num in enumerate(row):
            if num == pos:
                return x, y

def get_dests(pos):
    coords = get_coords(pos)
    dests = []
    for vector in KNIGHT_VECTORS:
        x, y = vectorsum(coords, vector)
        if 0 <= x < 8 and 0 <= y < 8:
            dests.append(BOARD[y][x])
    return dests

def solution(src, dest):
    to_search = deque()
    searched = []
    paths_to_cell = defaultdict(list)

    to_search.append(src)
    while True:
        start_cell = to_search.popleft()
        if not start_cell == dest:
            for end_cell in get_dests(start_cell):
                if end_cell in searched:
                    continue
                elif end_cell not in to_search:
                    paths_to_cell[end_cell] = paths_to_cell[start_cell] + [end_cell]
                    to_search.append(end_cell)

            searched.append(start_cell)
        else:
            return len(paths_to_cell[dest])

import unittest
class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(solution(0, 1), 3)
        self.assertEqual(solution(19, 36), 1)