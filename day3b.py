# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import string


def to_priority(char):
    if char in string.ascii_lowercase:
        return ord(char) - ord('a') + 1
    if char in string.ascii_uppercase:
        return ord(char) - ord('A') + 27


total = 0
with open('day3.dat') as f:
    while True:
        a = f.readline().strip()
        if a == '':
            break
        b = f.readline().strip()
        c = f.readline().strip()
        badge = (set(a) & set(b) & set(c)).pop()
        total += to_priority(badge)

print(total)
