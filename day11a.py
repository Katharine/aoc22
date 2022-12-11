# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

class Monkey:
    def __init__(self, items, operation, test, true_dest, false_dest):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspections = 0

monkeys = [
    Monkey(
        items=[96, 60, 68, 91, 83, 57, 85],
        operation=lambda x: x * 2,
        test=lambda x: (x % 17) == 0,
        true_dest=2,
        false_dest=5),

    Monkey(
        items=[75, 78, 68, 81, 73, 99],
        operation=lambda x: x + 3,
        test=lambda x: (x % 13) == 0,
        true_dest=7,
        false_dest=4),

    Monkey(
        items=[69, 86, 67, 55, 96, 69, 94, 85],
        operation=lambda x: x + 6,
        test=lambda x: (x % 19) == 0,
        true_dest=6,
        false_dest=5),

    Monkey(
        items=[88, 75, 74, 98, 80],
        operation=lambda x: x + 5,
        test=lambda x: (x % 7) == 0,
        true_dest=7,
        false_dest=1),

    Monkey(
        items=[82],
        operation=lambda x: x + 8,
        test=lambda x: (x % 11) == 0,
        true_dest=0,
        false_dest=2),

    Monkey(
        items=[72, 92, 92],
        operation=lambda x: x * 5,
        test=lambda x: (x % 3) == 0,
        true_dest=6,
        false_dest=3),

    Monkey(
        items=[74, 61],
        operation=lambda x: x * x,
        test=lambda x: (x % 2) == 0,
        true_dest=3,
        false_dest=1),

    Monkey(
        items=[76, 86, 83, 55],
        operation=lambda x: x + 4,
        test=lambda x: (x % 5) == 0,
        true_dest=4,
        false_dest=0),
]

for round in range(20):
    for monkey in monkeys:
        while monkey.items:
            monkey.inspections += 1
            item = monkey.items.pop(0)
            item = monkey.operation(item)
            item //= 3
            if monkey.test(item):
                monkeys[monkey.true_dest].items.append(item)
            else:
                monkeys[monkey.false_dest].items.append(item)

counts = sorted(monkey.inspections for monkey in monkeys)
print(counts)
print(counts[-1] * counts[2])
