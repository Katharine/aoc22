# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

mapping = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

def match_score(a, b):
    b = mapping[b]
    if a == b:
        return 3
    if (a, b) in [('A', 'C'), ('B', 'A'), ('C', 'B')]:
        return 0
    return 6

def shape_score(shape):
    return scores[mapping.get(shape, shape)]


score = 0
with open('day2.dat') as f:
    for line in f:
        a, b = line.strip().split()
        score += match_score(a, b) + shape_score(b)

print(score)
