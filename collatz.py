#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : collatz.py
# @Date : 2020-02-10
# @Author : Wufei Ma


def step(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError('Input parameter n is not an integer.')
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1


def summary(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError('Input parameter n is not an integer.')
    print(n, end='')
    count = 0
    while True:
        n = step(n)
        print(' => {:d}'.format(n), end='')
        count += 1
        if n == 1:
            break
    print('\n{:d} steps'.format(count))


if __name__ == '__main__':

    """
    x = 7
    count = 0
    while True:
        print(x)
        if x == 1:
            break
        else:
            x = step(x)
            count += 1
    print('Took {:d} iterations'.format(count))
    """

    summary(7)
