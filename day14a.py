# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

world = []
for y in range(220):
    world.append([' '] * 510)

with open('day14.dat') as f:
    for line in f:
        path = [tuple(map(int, x.split(','))) for x in line.strip().split(' -> ')]
        origin_x, origin_y = path.pop(0)
        print("start path")
        for (dest_x, dest_y) in path:
            print(f"({origin_x}, {origin_y}) -> {dest_x}, {dest_y}")
            if dest_y == origin_y:
                if dest_x > origin_x:
                    for x_i in range(origin_x, dest_x + 1):
                        world[origin_y][x_i] = '#'
                else:
                    for x_i in range(dest_x, origin_x + 1):
                        world[origin_y][x_i] = '#'
            else:
                if dest_y > origin_y:
                    for y_i in range(origin_y, dest_y + 1):
                        world[y_i][origin_x] = '#'
                else:
                    for y_i in range(dest_y, origin_y + 1):
                        world[y_i][origin_x] = '#'
            origin_x, origin_y = dest_x, dest_y



def process_sand():
    sand_x, sand_y = 500, 0
    while True:
        if sand_y >= 200:
            return None
        if world[sand_y+1][sand_x] == ' ':
            sand_y += 1
            continue
        if world[sand_y+1][sand_x-1] == ' ':
            sand_x -= 1
            continue
        if world[sand_y+1][sand_x+1] == ' ':
            sand_x += 1
            continue
        return sand_x, sand_y


sands = 0
while True:
    next_sand = process_sand()
    if next_sand is None:
        break
    world[next_sand[1]][next_sand[0]] = 'o'
    sands += 1

for row in world:
    print("".join(row))

print(sands)
