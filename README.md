# Collatz Conjecture

## Problem

The **Collatz Conjecture** is a conjecture in mathematics that conerns a sequence defined as follows: start with any positive integer $n$. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of $n$, the sequence will always reach 1.

*From Wikipedia*

In other words, given any positive integer $n$, we have such sequence of integers where the first element is $n$, and every other element equals the previous element transformed by $f$ where

$$f(n) = \begin{cases}n / 2 & \text{ if $n$ is even } \\ 3n + 1 & \text{ if $n$ is odd }\end{cases}$$
