# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0
import functools
import re

valves = {}

class Valve:
    def __init__(self, name: str, flow: int, tunnels: list[str]):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels


def pressure_for_valves(vs: frozenset[str]):
    return sum(valves[x].flow for x in vs)


@functools.cache
def try_option(valve: str, total_pressure: int, remaining_minutes: int, currently_open: frozenset[str]):
    if remaining_minutes == 0:
        return total_pressure
    v = valves[valve]
    best_option = 0
    if valve not in currently_open:
        if v.flow != 0:
            p = try_option(valve, total_pressure + pressure_for_valves(currently_open), remaining_minutes - 1, currently_open | frozenset([valve]))
            if p > best_option:
                best_option = p
    for tunnel in v.tunnels:
        p = try_option(tunnel, total_pressure + pressure_for_valves(currently_open), remaining_minutes - 1, currently_open)
        if p > best_option:
            best_option = p
    return best_option


with open('day16.dat') as f:
    for line in f:
        if line.strip() == "":
            continue
        print(line)
        m = re.match(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line.strip())
        valves[m.group(1)] = Valve(m.group(1), int(m.group(2)), m.group(3).split(', '))

print(try_option('AA', 0, 30, frozenset()))
