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
        print(f"({sensor.location.x}, {sensor.location.y}): ", dist, dist_from_bar, blocked_range)
        return blocked_range

    return None


def main():
    sensors = []
    with open('day15.dat') as f:
        for line in f:
            result = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line.strip())
            sensors.append(Sensor(Point(int(result.group(1)), int(result.group(2))), Point(int(result.group(3)), int(result.group(4)))))

    blocked_coords = set()
    for sensor in sensors:
        blocked = sensor_intersection(2000000, sensor)
        if blocked is None:
            continue
        for x in range(blocked[0], blocked[1] + 1):
            blocked_coords.add(x)

        for sensor in sensors:
            if sensor.closest_beacon.y == 2000000 and sensor.closest_beacon.x in blocked_coords:
                blocked_coords.remove(sensor.closest_beacon.x)

    print(len(blocked_coords))


main()
