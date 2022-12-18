# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import collections
import functools

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


@functools.cache
def find_air_connections(drop: Cube) -> list[Cube]:
    connections = []
    for adj in adjacencies:
        c = Cube(drop.x + adj[0], drop.y + adj[1], drop.z + adj[2])
        if c not in droplets:
            connections.append(c)
    return connections


def has_path_to_air(origin: Cube):
    visited = set()
    q = collections.deque(find_air_connections(origin))
    while q:
        step = q.popleft()
        if step in visited:
            continue
        visited.add(step)
        if step.x < 1 or step.x > 20 or step.y < 1 or step.y > 20 or step.z < 1 or step.z > 20:
            return True
        q.extend(find_air_connections(step))

real_droplets = droplets.copy()

for x in range(1, 20):
    for y in range(1, 20):
        for z in range(1, 20):
            if Cube(x, y, z) in droplets:
                continue
            c = Cube(x, y, z)
            if not has_path_to_air(c):
                real_droplets.add(c)

for drop in real_droplets:
    for adj in adjacencies:
        if Cube(drop.x + adj[0], drop.y + adj[1], drop.z + adj[2]) not in real_droplets:
            free_sides += 1

print(free_sides)
