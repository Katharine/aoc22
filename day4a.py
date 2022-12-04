# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

def split(e):
    return tuple(int(x) for x in e.split('-'))


def contains(range1, range2):
    print(range1, range2)
    return (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range2[0] >= range1[0] and range2[1] <= range1[1])

contained = 0
with open('day4.dat') as f:
    for line in f:
        elves = line.strip().split(',')
        if contains(split(elves[0]), split(elves[1])):
            contained += 1

print(contained)
