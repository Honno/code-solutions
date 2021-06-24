#!/usr/bin/env python2
from collections import defaultdict
import Queue

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
FREE, WALL = 0, 1

class OutOfMapBoundaryError(Exception):
    pass

class Ship:
    def __init__(self, map_):
        self.h = len(map_)
        self.w = len(map_[0])

        cells_map = [[Cell(state) for state in row] for row in map_]
        self.start = cells_map[0][0]
        self.end = cells_map[self.h-1][self.w-1]

        for y, row in enumerate(cells_map):
            for x, cell in enumerate(row):
                cell.coord = (x, y)
                for vector in DIRECTIONS:
                    try:
                        target_x, target_y = self._point((x, y), vector)
                        neighbour = cells_map[target_y][target_x]
                        cell.add_adjacent(neighbour)
                    except OutOfMapBoundaryError:
                        pass

        self.cells = [cell for row in cells_map for cell in row]

    def _point(self, *vectors):
        x = sum(v[0] for v in vectors)
        y = sum(v[1] for v in vectors)
        if not 0 <= x < self.w or not 0 <= y < self.h:
            raise OutOfMapBoundaryError
        else:
            return x, y

    def get_free(self):
        return [cell for cell in self.cells if cell.state == FREE]

    def get_walls(self):
        return [cell for cell in self.cells if cell.state == WALL]

class Cell:
    def __init__(self, state):
        self.state = state
        self.adjacent = []
        self.coord = None

    def add_adjacent(self, cell):
        self.adjacent.append(cell)

    @property
    def neighbours(self):
        return [cell for cell in self.adjacent if cell.state == FREE]

    def __repr__(self):
        return str(self.coord)

def heuristic(cell1, cell2):
    return sum((a - b) for a, b in zip(cell1.coord, cell2.coord))

# dont know how good I get it with python 3
# @dataclass(order=True)
# class PrioritisedItem:
#     priority: int
#     item: Any = field(compare=False)

def find_best_path(graph, start, end, stop_after_cost=float('inf'), middle=None):
    to_search = Queue.PriorityQueue()
    costs = {}

    if middle != None:
        dest = middle
    else:
        dest = end

    costs[start] = 0
    to_search.put((0, start))
    while not to_search.empty():
        origin = to_search.get()[1] # min dist u

        if origin == dest:
            if dest == end:
                return costs[end] + 1
            if dest == middle:
                if costs[middle] > stop_after_cost:
                    return float('inf')
                else:
                    dest = end

        for neighbour in origin.neighbours:
            cost = costs[origin] + 1
            if neighbour not in costs or cost < costs[neighbour]:
                costs[neighbour] = cost

                priority = heuristic(dest, neighbour)
                to_search.put((priority, neighbour))
    return float('inf')

def solution(map_):
    graph = Ship(map_)

    best_cost = find_best_path(graph, graph.start, graph.end)
    no_clip_cost = heuristic(graph.end, graph.start) + 1
    if best_cost > no_clip_cost:
        for cell in graph.get_walls():
            cell.state = FREE
            cost = find_best_path(graph, graph.start, graph.end,
                                  stop_after_cost=best_cost,
                                  middle=cell)
            cell.state = WALL

            if cost == no_clip_cost:
                return cost
            elif cost < best_cost:
                best_cost = cost
    return best_cost

from unittest import TestCase
class Tests(TestCase):
    def test1(self):
        self.assertEqual(solution([[0, 1, 1, 0],
                                   [0, 0, 0, 1],
                                   [1, 1, 0, 0],
                                   [1, 1, 1, 0]]), 7)
    def test2(self):
        self.assertEqual(solution([[0, 0, 0, 0, 0, 0],
                                   [1, 1, 1, 1, 1, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 1, 1, 1, 1, 1],
                                   [0, 1, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0]]), 11)

    def test_awkward(self):
        self.assertEqual(solution([[0, 0, 0, 0, 0, 0],
                                   [1, 1, 1, 0, 1, 1],
                                   [1, 1, 1, 0, 1, 1],
                                   [1, 0, 1, 0, 1, 1],
                                   [1, 0, 1, 1, 1, 1],
                                   [1, 0, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0, 0]]), 16)