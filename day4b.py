# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

ROOMS = 100


def split(e):
    return tuple(int(x) for x in e.split('-'))


def contains(range1, range2):
    rooms = [0] * ROOMS
    for room in range(range1[0], range1[1]+1):
        rooms[room] += 1
    for room in range(range2[0], range2[1]+1):
        rooms[room] += 1
    return any(room == 2 for room in rooms)


contained = 0
with open('day4.dat') as f:
    for line in f:
        elves = line.strip().split(',')
        if contains(split(elves[0]), split(elves[1])):
            contained += 1

print(contained)
