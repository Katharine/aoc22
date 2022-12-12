# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import string
import collections

origin = None
dest = None
with open('day12.dat') as f:
    heightmap = []
    for i, line in enumerate(f):
        line = line.strip()
        if line.find('S') != -1:
            origin = (line.index('S'), i)
            line = line.replace('S', 'a')
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


def main():
    queue = collections.deque()
    queue.extend([[origin, x] for x in next_steps(heightmap, origin)])
    visited = set()
    while len(queue):
        path = queue.popleft()
        steps = next_steps(heightmap, path[-1])
        for step in steps:
            if step == dest:
                print("done!")
                print(path + [step])
                print(len(path))
                return
            if step not in visited:
                visited.add(step)
                queue.append(path + [step])


main()
