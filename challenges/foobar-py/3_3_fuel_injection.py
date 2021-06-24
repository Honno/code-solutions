#!/usr/bin/env python2.7

#          .
#         -|-
#          |
#      .-'~~~`-.
#    .'         `.
#    |  R  I  P  |
#    |           |
#    | the cool  |
#    | recursive |
#    | solution  |
#  \\|           |//   jgs
# ^^^^^^^^^^^^^^^^^^^

def solution(n_str):
    n = int(n_str)
    nops = 0 # no. of operations

    while(n > 1):
        if n % 2 == 0:
            n = n / 2      # DIV
        else:
            if n == 3:
                nops += 2  # pretend DEL + DIV
                break

            if n % 4 != 1:
                n += 1     # ADD
            else:
                n -= 1     # DEL

        nops += 1

    return nops

from unittest import TestCase

class Tests(TestCase):
    def test1(self):
        assert solution("15") == 5

    def test2(self):
        assert solution("4") == 2

    def test3(self):
        assert solution("5") == 3

    def test4(self):
        assert solution("6") == 3
        assert solution("7") == 4

    def test5(self):
        assert solution("100") == 8
        assert solution("101") == 9

    def test6(self):
        solution(
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
            "01234567890123456789012345678901234567890123456789"
        )

    def test7(self):
        assert solution("3") == 2

#                                .-----------------------------.
#                                | Welcome to the UNDERWORLD!! |
#                                '--. .------------------------'
#   .-._                            |/                     _,-,
#    `._`-._                        `                  _,-'_,'
#       `._ `-._                                   _,-' _,'
#          `._  `-._        __.-----.__        _,-'  _,'
#             `._   `#==="""           """===#'   _,'
#                `._/)  ._               _.  (\_,'
#                 )*'     **.__     __.**     '*(
#                 #  .==..__  ""   ""  __..==,  #
#                 #   `"._(_).       .(_)_."'   #                Deelkar
# ------------------------------------------------------------------------------
#
# cache = {} # <n>: <nops>
#
# def min_nops(n):
#     if n == 1:
#         return 0 # NO-OP
#     elif n == 2:
#         return 1 # DIV
#
#     if n in cache:
#         return cache[n]
#
#     if n % 2 == 0:
#         nops = min_nops(n / 2) + 1 # DIV
#     else:
#         ceil_nops = min_nops(n + 1) + 1 # ADD, DIV
#         floor_nops = min_nops(n - 1) + 1 # DEL, DIV
#         nops = min(ceil_nops, floor_nops)
#
#     cache[n] = nops
#     return nops
#
# def solution(n_str):
#     n = int(n_str)
#     return min_nops(n)
