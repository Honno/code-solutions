#!/usr/bin/env python2.7
def solution(l):
    ntriples = 0
    for iy, y in enumerate(l[1:-1], 1):
        ix = iy - 1
        iz = iy + 1

        nfactors_xy = 0
        for x in l[:iy]:
            if y % x == 0:
                nfactors_xy += 1

        nfactors_yz = 0
        for z in l[iz:]:
            if z % y == 0:
                nfactors_yz += 1

        ntriples += nfactors_xy * nfactors_yz

    return ntriples

from unittest import TestCase

class Tests(TestCase):
    def test1(self):
        assert solution([1, 2, 3, 4, 5, 6]) == 3

    def test2(self):
        assert solution([1, 1, 1]) == 1

    def test3(self):
        assert solution([8, 4, 2, 1]) == 0

    def test4(self):
        assert solution([8, 4, 2, 1, 2, 4]) == 2
