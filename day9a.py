# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

from collections import namedtuple

Pos = namedtuple('Pos', ('x', 'y'))

head_pos = Pos(0, 0)
tail_pos = Pos(0, 0)

moves = {
    'U': Pos(0, -1),
    'L': Pos(-1, 0),
    'D': Pos(0, 1),
    'R': Pos(1, 0),
}

def tail_in_range(head: Pos, tail: Pos) -> bool:
    return abs(head.x - tail.x) <= 1 and abs (head.y - tail.y) <= 1

visited_positions = {Pos(0, 0)}

with open('day9.dat') as f:
    for line in f:
        direction, steps = line.strip().split()
        steps = int(steps)
        move = moves[direction]

        for step in range(steps):
            head_pos = Pos(head_pos.x + move.x, head_pos.y + move.y)
            if tail_in_range(head_pos, tail_pos):
                continue
            x_step = 0
            y_step = 0
            if tail_pos.x < head_pos.x:
                x_step = 1
            elif tail_pos.x > head_pos.x:
                x_step = -1
            if tail_pos.y < head_pos.y:
                y_step = 1
            elif tail_pos.y > head_pos.y:
                y_step = -1
            tail_pos = Pos(tail_pos.x + x_step, tail_pos.y + y_step)
            visited_positions.add(tail_pos)

print(len(visited_positions))
