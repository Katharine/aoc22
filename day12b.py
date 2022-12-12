# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import string
import collections

possible_origins = []
dest = None
with open('day12.dat') as f:
    heightmap = []
    for i, line in enumerate(f):
        line = line.strip()
        for j, char in enumerate(line):
            if char == 'a':
                possible_origins.append((j, i))
        if line.find('E') != -1:
            dest = (line.index('E'), i)
            line = line.replace('E', 'z')
        heightmap.append([string.ascii_lowercase.index(x) for x in line])


def next_steps(heightmap, pos):
    options = []
    for (x, y) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        new_pos = (pos[0] + x, pos[1] + y)
        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(heightmap[0]) or new_pos[1] >= len(heightmap):
            continue
        if heightmap[pos[1] + y][pos[0] + x] <= heightmap[pos[1]][pos[0]] + 1:
            options.append(new_pos)
    return options


def find_route(origin):
    queue = collections.deque()
    queue.extend([[origin, x] for x in next_steps(heightmap, origin)])
    visited = set()
    while len(queue):
        path = queue.popleft()
        steps = next_steps(heightmap, path[-1])
        for step in steps:
            if step == dest:
                return len(path)
            if step not in visited:
                visited.add(step)
                queue.append(path + [step])
    return None


shortest_route = None
for o in possible_origins:
    new_len = find_route(o)
    if new_len is not None and (shortest_route is None or new_len < shortest_route):
        print(f"new best: {new_len}")
        shortest_route = new_len

print(shortest_route)
