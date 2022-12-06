# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

with open('day6.dat') as f:
    text = f.readline().strip()

last_four = ''
for i in range(len(text)):
    last_four += text[i]
    if len(set(last_four)) == 14:
        print(i)
        break
    if len(last_four) >= 14:
        last_four = last_four[1:]
