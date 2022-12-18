# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import collections

Cube = collections.namedtuple('Cube', ('x', 'y', 'z'))

droplets = set()

with open('day18.dat') as f:
    for line in f:
        droplets.add(Cube(*map(int, line.strip().split(','))))

free_sides = 0

adjacencies = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
]

for drop in droplets:
    for adj in adjacencies:
        if Cube(drop.x + adj[0], drop.y + adj[1], drop.z + adj[2]) not in droplets:
            free_sides += 1

print(free_sides)
