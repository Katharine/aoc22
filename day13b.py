# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import json
import functools

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

all_packets = [json.loads(x.strip()) for x in data if x.strip() != ""]

sorted_packets = sorted(all_packets, key=functools.cmp_to_key(lambda a, b: (-1 if do_compare(a, b) else 1)))
print(sorted_packets)

result = 1
for i, packet in enumerate(sorted_packets):
    print(packet)
    if len(packet) == 1 and isinstance(packet[0], list) and len(packet[0]) == 1:
        if packet[0][0] in (2, 6):
            print(i, packet)
            result *= (i + 1)

print(result)