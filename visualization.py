#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename : visualization.py
# @Date : 2020-02-10
# @Author : Wufei Ma

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import collatz


if __name__ == '__main__':

    df = pd.DataFrame(columns=['initial', 'maximum', 'iterations'])
    for i in range(1, 500):
        x = i
        maximum = i
        count = 0
        while True:
            if x == 1:
                break
            else:
                x = collatz.step(x)
                maximum = max(maximum, x)
                count += 1
        df = df.append({
            'initial': i,
            'maximum': maximum,
            'iterations': count
        }, ignore_index=True)

    print(df)
    exit()

    plt.figure(figsize=(10, 10))
    plt.subplot(211)
    plt.plot(df['initial'], df['maximum'])
    plt.title('Max Integer Reached')
    plt.subplot(212)
    plt.plot(df['initial'], df['iterations'])
    plt.title('Number of Iterations')
    plt.suptitle('Collatz Conjecture Visualization')
    plt.savefig('visualization.png', dpi=200)
