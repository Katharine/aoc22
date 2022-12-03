# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import string

def to_priority(char):
    if char in string.ascii_lowercase:
        return ord(char) - ord('a') + 1
    if char in string.ascii_uppercase:
        return ord(char) - ord('A') + 27


def split_bag(s):
    return s[:len(s)//2], s[len(s)//2:]


def common(a, b):
    return set(a) & set(b)


def score_bag(b):
    a, b = split_bag(b)
    c = common(a, b)
    return sum(to_priority(x) for x in c)


total = 0
with open('day3.dat') as f:
    for line in f:
        total += score_bag(line.strip())

print(total)
