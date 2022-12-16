# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import collections
import functools
import re


class Valve:
    def __init__(self, name: str, flow: int, tunnels: list[str]):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels


def get_real_valves(valves):
    return {k: v for k, v in valves.items() if v.flow > 0}


def find_valve_path(valves: dict[str, Valve], origin: str, dest: str):
    visited = set()
    queue = collections.deque()
    queue.extend([origin, x] for x in valves[origin].tunnels)
    while len(queue) > 0:
        path = queue.popleft()
        if path[-1] == dest:
            return len(path)
        for tunnel in valves[path[-1]].tunnels:
            if tunnel not in visited:
                queue.append(path + [tunnel])


def generate_valve_graph(valves: dict[str, Valve]):
    real_valves = get_real_valves(valves)
    valve_adjacency = {}
    for v1 in {'AA': valves['AA'], **real_valves}:
        valve_adjacency[v1] = {}
        for v2 in real_valves:
            if v2 == v1:
                continue
            valve_adjacency[v1][v2] = find_valve_path(valves, v1, v2)
    return valve_adjacency


Step = collections.namedtuple('Step', ('valve', 'open_time'))

TIME_LIMIT = 30


def score_path(path: list[Step]):
    score = 0
    for p in path:
        v = valves[p.valve]
        score += v.flow * (TIME_LIMIT - p.open_time)
    return score


@functools.cache
def possible_single_paths(start: str, time_spent: int, excluded: frozenset[str], must_exhaust=False) -> list[list[Step]]:
    paths = []
    for next, cost in valve_adjacency[start].items():
        if next in excluded:
            continue
        if cost >= TIME_LIMIT - time_spent:
            continue
        next_paths = possible_single_paths(next, time_spent + cost, excluded | {next}, must_exhaust=must_exhaust)
        for path in next_paths:
            paths.append([Step(start, time_spent)] + path)
    if len(paths) == 0 or must_exhaust:
        paths.append([Step(start, time_spent)])
    return paths


valves = {}
with open('day16.dat') as f:
    for line in f:
        if line.strip() == "":
            continue
        print(line)
        m = re.match(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line.strip())
        valves[m.group(1)] = Valve(m.group(1), int(m.group(2)), m.group(3).split(', '))

valve_adjacency = generate_valve_graph(valves)


def main():
    print(f"Generated valve adjacency")
    print(valve_adjacency)
    possible_paths = possible_single_paths('AA', 0, frozenset(), must_exhaust=True)
    print(len(possible_paths))
    best_score = 0
    best_path = []
    for human_counter, path in enumerate(possible_paths):
        if human_counter % 100 == 0:
            print(f"{human_counter} / {len(possible_paths)} ({human_counter/len(possible_paths)*100:.2f}%)")
        score = score_path(path)
        if score > best_score:
            best_score = score
            best_path = path
            print(f"new best score {best_score}: {best_path}")

    print("DONE!")
    print(best_score)
    print(best_path)

main()
