# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day8.dat') as f:
    grid = [list(map(int, x.strip())) for x in f.readlines() if x.strip() != ""]

WIDTH = len(grid[0])
HEIGHT = len(grid)

visible_trees = set()

for x in range(WIDTH):
    current_height = -1
    for y in range(HEIGHT):
        if grid[x][y] > current_height:
            visible_trees.add((x, y))
            current_height = grid[x][y]

for x in range(WIDTH):
    current_height = -1
    for y in range(HEIGHT - 1, -1, -1):
        if grid[x][y] > current_height:
            visible_trees.add((x, y))
            current_height = grid[x][y]

for y in range(HEIGHT):
    current_height = -1
    for x in range(WIDTH):
        if grid[x][y] > current_height:
            visible_trees.add((x, y))
            current_height = grid[x][y]

for y in range(HEIGHT):
    current_height = -1
    for x in range(WIDTH - 1, -1, -1):
        if grid[x][y] > current_height:
            visible_trees.add((x, y))
            current_height = grid[x][y]

print(len(visible_trees))
