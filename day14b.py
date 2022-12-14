# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

world = set()

max_y = 0
with open('day14.dat') as f:
    for line in f:
        path = [tuple(map(int, x.split(','))) for x in line.strip().split(' -> ')]
        origin_x, origin_y = path.pop(0)
        if origin_y > max_y:
            max_y = origin_y
        for (dest_x, dest_y) in path:
            if dest_y > max_y:
                max_y = dest_y
            if dest_y == origin_y:
                if dest_x > origin_x:
                    for x_i in range(origin_x, dest_x + 1):
                        world.add((x_i, origin_y))
                else:
                    for x_i in range(dest_x, origin_x + 1):
                        world.add((x_i, origin_y))
            else:
                if dest_y > origin_y:
                    for y_i in range(origin_y, dest_y + 1):
                        world.add((origin_x, y_i))
                else:
                    for y_i in range(dest_y, origin_y + 1):
                        world.add((origin_x, y_i))
            origin_x, origin_y = dest_x, dest_y

y_floor = max_y + 2


def process_sand():
    sand_x, sand_y = 500, 0
    while True:
        if sand_y+1 == y_floor:
            return sand_x, sand_y
        if (sand_x, sand_y + 1) not in world:
            sand_y += 1
            continue
        if (sand_x - 1, sand_y + 1) not in world:
            sand_x -= 1
            continue
        if (sand_x + 1, sand_y + 1) not in world:
            sand_x += 1
            continue
        return sand_x, sand_y


sands = 0
while True:
    next_sand = process_sand()
    sands += 1
    if next_sand == (500, 0):
        break
    world.add(next_sand)

print(sands)
