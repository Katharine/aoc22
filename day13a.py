# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import json

with open('day13.dat') as f:
    data = f.readlines()


def do_compare(a: int | list, b: int | list):
    if isinstance(a, int) != isinstance(b, int):
        if isinstance(a, int):
            return do_compare([a], b)
        else:
            return do_compare(a, [b])
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b
    for (a_i, b_i) in zip(a, b):
        result = do_compare(a_i, b_i)
        if result is not None:
            return result
    if len(a) < len(b):
        return True
    if len(a) > len(b):
        return False
    return None

in_order = []

for i in range(0, len(data), 3):
    packet_a = json.loads(data[i])
    packet_b = json.loads(data[i+1])

    print(packet_a)
    print(packet_b)
    if do_compare(packet_a, packet_b):
        print("in order!")
        in_order.append(i // 3 + 1)
    else:
        print("not in order!")

print(sum(in_order))
