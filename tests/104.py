#!/usr/bin/env python
# -*- coding: utf8 -*-

import copy


def mx(a, b):
    return [
        [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1]
        ],
        [
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1]
        ]
    ]


def fastfib(n):
    s = bin(n)[3:]
    m = [[1, 1], [1, 0]]
    ret = m
    for c in s:
        if c == '0':
            ret = mx(ret, ret)
        else:
            ret = mx(ret, ret)
            ret = mx(ret, m)
    return ret[0][1]


pandigits = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

pf2 = 1
pf1 = 1
k = 3
while True:
    f = (pf1 + pf2) % 100000000000
    pf1, pf2 = f, pf1
    last = str(f)[-9:]

    if set(last) == pandigits:
        print k
        f = fastfib(k)
        if set(str(f)[:9]) == pandigits:
            print "SOLUTION:", k
            exit()

    k += 1
    if k % 10000 == 0:
        print '*'
