# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

winners = {'A': 'C', 'B': 'A', 'C': 'B'}
losers = {'C': 'A', 'A': 'B', 'B': 'C'}

def match_score(a, b):
    if a == b:
        return 3
    if (a, b) in [('A', 'C'), ('B', 'A'), ('C', 'B')]:
        return 0
    return 6


def shape_picker(them, target):
    if target == 'Y':
        return them
    if target == 'Z':
        return losers[them]
    return winners[them]


def shape_score(shape):
    return scores[shape]


score = 0
with open('day2.dat') as f:
    for line in f:
        them, b = line.strip().split()
        me = shape_picker(them, b)
        score += match_score(them, me) + shape_score(me)

print(score)
