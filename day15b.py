# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import re


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Sensor:
    def __init__(self, location: Point, closest_beacon: Point):
        self.location = location
        self.closest_beacon = closest_beacon

    def beacon_distance(self):
        return abs(self.location.x - self.closest_beacon.x) + abs(self.location.y - self.closest_beacon.y)


def sensor_intersection(row: int, sensor: Sensor):
    dist = sensor.beacon_distance()
    dist_from_bar = abs(row - sensor.location.y)
    if dist_from_bar <= dist:
        blocked_amount = (dist - dist_from_bar) * 2 + 1
        blocked_range = (sensor.location.x - blocked_amount // 2, sensor.location.x + blocked_amount // 2)
        return blocked_range

    return None


def merge_intervals(intervals: list[tuple[int, int]]):
    intervals = sorted(intervals)
    i = 0
    while i + 1 < len(intervals):
        a = intervals[i]
        b = intervals[i+1]
        if a[1] < b[0]:  # a ends before b starts; disjoint
            i += 1
            continue
        if a[1] >= b[1]:  # a ends after b ends; fully enclosed
            del intervals[i+1]
            continue
        if a[1] >= b[0]:  # a ends inside b; merge
            intervals[i] = (a[0], b[1])
            del intervals[i+1]
    return intervals


MAGIC_NUMBER = 4000000


def main():
    sensors = []
    with open('day15.dat') as f:
        for line in f:
            result = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line.strip())
            sensors.append(Sensor(Point(int(result.group(1)), int(result.group(2))), Point(int(result.group(3)), int(result.group(4)))))

    for row in range(MAGIC_NUMBER):
        if row % 10000 == 0:
            print(f"row {row}")

        ranges = []
        for sensor in sensors:
            blocked = sensor_intersection(row, sensor)
            if blocked is None:
                continue
            ranges.append((max(blocked[0], 0), min(blocked[1], MAGIC_NUMBER)))
        merged = merge_intervals(ranges)
        if len(merged) > 1 or merged[0][0] != 0 or merged[0][1] != MAGIC_NUMBER:
            print("got it!")
            print(row)
            print(merged)
            print(f"answer is: {(merged[0][1] + 1) * MAGIC_NUMBER + row}")
            return

main()