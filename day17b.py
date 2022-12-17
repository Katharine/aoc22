# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0
import collections
from tqdm import tqdm

Coord = collections.namedtuple('Coord', ('x', 'y'))

ROCKS = [
    [Coord(0, 1), Coord(1, 1), Coord(2, 1), Coord(3, 1)],
    [Coord(1, 1), Coord(0, 2), Coord(1, 2), Coord(2, 2), Coord(1, 3)],
    [Coord(0, 1), Coord(1, 1), Coord(2, 1), Coord(2, 2), Coord(2, 3)],
    [Coord(0, 1), Coord(0, 2), Coord(0, 3), Coord(0, 4)],
    [Coord(0, 1), Coord(0, 2), Coord(1, 1), Coord(1, 2)]
]


class World:
    def __init__(self, jets: str):
        self.jets = jets
        self.jet_index = 0
        self.rocks = set()
        self.height = 0
        self.next_rock = 0
        self.row_tracker = {}
        self.bottom = 0

    def drop_rock(self):
        rock = ROCKS[self.next_rock]
        self.next_rock = (self.next_rock + 1) % len(ROCKS)
        x = 2
        y = self.height + 3
        self.process_rock(rock, x, y)

    def process_rock(self, rock: list[Coord], x: int, y: int):
        while True:
            # process a shift
            shift = 1 if self.jets[self.jet_index] == '>' else -1
            self.jet_index = (self.jet_index + 1) % len(self.jets)
            if not self.rock_collides(rock, x + shift, y):
                x += shift
            # process a drop
            new_y = y - 1
            if self.rock_collides(rock, x, new_y):
                self.install_rock(rock, x, y)
                return
            else:
                y = new_y

    def install_rock(self, rock: list[Coord], x: int, y: int):
        max_height = 0
        for c in rock:
            if c.y + y > max_height:
                max_height = c.y + y
            self.rocks.add((c.x + x, c.y + y))
            self.row_tracker[c.y+y] = self.row_tracker.get(c.y+y, 0) + 1
            if self.row_tracker[c.y+y] == 7:
                self.bottom = c.y+y
                new_rocks = set()
                for r in self.rocks:
                    if r[1] > self.bottom:
                        new_rocks.add(r)
                self.rocks = new_rocks
        if max_height > self.height:
            self.height = max_height

    def rock_collides(self, rock: list[Coord], x: int, y: int):
        for c in rock:
            if c.x + x < 0 or c.x + x >= 7 or c.y + y <= self.bottom:
                return True
            if (c.x + x, c.y + y) in self.rocks:
                return True
        return False


def main():
    with open('day17.dat') as f:
        inp = f.readline().strip()
    world = World(inp)
    target = 1000000000000
    round_length = len(inp) * 5
    # these various numbers are presumably specific to my input
    repeat_length = round_length * 346
    loops = (target - round_length) // repeat_length
    start_height = 77560 + 26831969 * loops
    remaining_rocks = (target - round_length) % repeat_length
    world.jet_index = 1631
    for i in tqdm(range(remaining_rocks)):
        world.drop_rock()
    print(world.height, world.height + start_height)


main()
