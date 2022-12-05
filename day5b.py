# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0


import re
def parse_stacks(text: list[str]):
    stacks = [[] for x in range(len(text[-1].strip().split()))]
    for line in text[:-1][::-1]:
        line = line[:-1]
        for i in range(len(stacks)):
            if len(line) < i *4 + 1:
                continue
            entry = line[i*4+1]
            if entry != " ":
                stacks[i].append(entry)
    return stacks


def do_move(entry: str, stacks: list[list[str]]):
    m = re.match(r'move (\d+) from (\d+) to (\d+)', entry)
    amount = int(m.group(1))
    origin = int(m.group(2)) - 1
    dest = int(m.group(3)) - 1

    stacks[dest].extend(stacks[origin][-amount:])
    stacks[origin] = stacks[origin][:-amount]


with open('day5.dat') as f:
    stack_text = []
    for line in f:
        if line.strip() == "":
            break
        stack_text.append(line)

    stacks = parse_stacks(stack_text)

    for line in f:
        do_move(line.strip(), stacks)

print(''.join(s[-1] for s in stacks))
