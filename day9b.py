# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

from collections import namedtuple

Pos = namedtuple('Pos', ('x', 'y'))

moves = {
    'U': Pos(0, -1),
    'L': Pos(-1, 0),
    'D': Pos(0, 1),
    'R': Pos(1, 0),
}


def tail_in_range(head: Pos, tail: Pos) -> bool:
    return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1


def new_pos(head_pos: Pos, tail_pos: Pos) -> Pos:
        if tail_in_range(head_pos, tail_pos):
            return tail_pos
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
        return Pos(tail_pos.x + x_step, tail_pos.y + y_step)


visited_positions = {Pos(0, 0)}
segments = [Pos(0, 0)] * 10

with open('day9.dat') as f:
    for line in f:
        direction, steps = line.strip().split()
        steps = int(steps)
        move = moves[direction]

        for step in range(steps):
            segments[0] = Pos(segments[0].x + move.x, segments[0].y + move.y)
            for i in range(1, len(segments)):
                segments[i] = new_pos(segments[i-1], segments[i])
            visited_positions.add(segments[-1])

print(len(visited_positions))
