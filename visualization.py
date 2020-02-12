#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : visualization.py
# @Date : 2020-02-10
# @Author : Wufei Ma

import os
import sys

import math

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import collatz


if __name__ == '__main__':

    df = pd.DataFrame(columns=['initial', 'maximum', 'iterations', 'ratio'])
    for i in range(1, 200001):
        x = i
        start = i
        maximum = i
        count = 0
        while True:
            ratio = maximum / start
            if x == 1:
                break
            else:
                x = collatz.step(x)
                maximum = max(maximum, x)
                count += 1
        df = df.append({
            'initial': i,
            'maximum': maximum,
            'iterations': count,
            'ratio': ratio
        }, ignore_index=True)

    print(df)

    plt.figure(figsize=(10, 12))
    plt.subplot(311)
    plt.plot(df['initial'], df['maximum'])
    plt.title('Max Integer Reached')
    plt.subplot(312)
    plt.plot(df['initial'], df['iterations'])
    plt.title('Number of Iterations')
    plt.subplot(313)
    plt.plot(df['initial'], df['ratio'])
    plt.title('Maximum Integer Reached / n')
    plt.suptitle('Collatz Conjecture Visualization')
    plt.savefig('visualization.png', dpi=200)
