# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

interesting = []
def incr_cycle(c, n):
    for i in range(n):
        c += 1
        if c in (20, 60, 100, 140, 180, 220):
            interesting.append(c*x)
            print(c, x, c*x)
    return c

x = 1
cycle = 0
with open('day10.dat') as f:
    for line in f:
        instruction = line.strip()
        if instruction == "noop":
            cycle = incr_cycle(cycle, 1)
            continue
        instruction = instruction.split()
        if instruction[0] == "addx":
            cycle = incr_cycle(cycle, 2)
            x += int(instruction[1])

print(sum(interesting))