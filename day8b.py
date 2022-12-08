# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day8.dat') as f:
    grid = [list(map(int, x.strip())) for x in f.readlines() if x.strip() != ""]

WIDTH = len(grid[0])
HEIGHT = len(grid)


def scenic_score(trees, pos):
    tree_x, tree_y = pos
    height = trees[tree_y][tree_x]
    right, left, up, down = 0, 0, 0, 0
    for x in range(tree_x+1, WIDTH):
        right += 1
        if trees[tree_y][x] >= height:
            break

    for x in range(tree_x-1, -1, -1):
        left += 1
        if trees[tree_y][x] >= height:
            break

    for y in range(tree_y+1, HEIGHT):
        down += 1
        if trees[y][tree_x] >= height:
            break

    for y in range(tree_y-1, -1, -1):
        up += 1
        if trees[y][tree_x] >= height:
            break

    return right * left * up * down


best_score = 0
for x in range(WIDTH):
    for y in range(HEIGHT):
        new_score = scenic_score(grid, (x, y))
        if new_score > best_score:
            best_score = new_score

print(best_score)
