#!/usr/bin/env python2

from collections import deque
from itertools import permutations

def gen_permutations(numbers, slice_by):
    subsequence_len = len(numbers) - slice_by
    for permutation in permutations(numbers, subsequence_len):
        yield permutation

def permutations_tree(numbers):
    for i in range(len(numbers)):
        for permutation in gen_permutations(numbers, i):
            yield permutation

def solution(stamps):
    stamps = [str(stamp) for stamp in stamps]
    stamps.sort(reverse = True) # high to low
    for permutation in permutations_tree(stamps):
        code = int(''.join(permutation))
        if code % 3 == 0:
            return code
    else:
        return 0

from unittest import TestCase
class Tests(TestCase):
    def test1(self):
        self.assertEqual(solution([3, 1, 4, 1]), 4311)
    def test2(self):
        self.assertEqual(solution([3, 1, 4, 1, 5, 9]), 94311)
    def test_two_stamps(self):
        self.assertEqual(solution([2, 3]), 3)
    def test_one_stamp(self):
        self.assertEqual(solution([3]), 3)