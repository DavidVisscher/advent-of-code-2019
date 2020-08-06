"""
Advent of Code - Day 3

Wire tracer
"""

import sys

from tqdm import tqdm

from wiregrid import WireGrid


def main():
    """
    WireGrid simulation main function.
    """
    raw_wires = read_input_file();

    wire_data = []
    for raw_wire in tqdm(raw_wires, desc="Reading wire data"):
        wire_data.append(format_wire_data(raw_wire))

    grid = WireGrid()

    for nr, wire in tqdm(enumerate(wire_data), desc="Laying Wire"):
        lay_wire(wire, grid, nr)

    crossings = grid.crossings

    print("Shortest manhattan distance:")
    print(shortest_manhattan_distance(grid.crossings))
    
    print("Shortest wire distance:")
    print(shortest_combined_wire_path(grid))


def read_input_file(filename="wires.txt"):
    """
    Reads all raw wires from disk.
    """
    raw_wires = []
    with open(filename, 'r') as wirefile:
        raw_wires = wirefile.readlines()
    return raw_wires
    

def format_wire_data(raw_wire):
    """
    Receives wire input in the form:
    'R75,D30,R83,U83,L12,D49,R71,U7,L72' as a str.

    Outputs:
    ['R', 'R', ..., 'R', 'D', ...]
    """
    out = []

    instructions = raw_wire.split(',')

    for instr in instructions:
        instr = instr.strip()
        direction = instr[:1]
        distance = int(instr[1:])
        for _ in range(distance):
            out.append(direction)

    return out


def lay_wire(wire, grid, marker):
    """
    Lays the processed wires onto the wiregrid.
    """
    cursor = [0, 0]
    current_distance = 0

    for instr in wire:
        current_distance += 1

        if instr == 'R':
            cursor = (cursor[0] + 1, cursor[1])
        if instr == 'L':
            cursor = (cursor[0] - 1, cursor[1])
        if instr == 'U':
            cursor = (cursor[0], cursor[1] + 1)
        if instr == 'D':
            cursor = (cursor[0], cursor[1] -1)
        
        if not is_self_crossing(cursor, marker, grid):
            wire_data = {'marker': marker, 'distance': current_distance}
            grid.add(cursor[0], cursor[1], wire_data)

def is_self_crossing(cursor, marker, grid):
    """
    Checks if wire already runs through a cursor position,
    identified by the wire's marker.
    """
    grid_point_wires = grid.get(cursor[0], cursor[1])

    for wire in grid_point_wires:
        if wire['marker'] == marker:
            return True
    return False


def shortest_manhattan_distance(coordinates):
    """
    Calculates the shortest manhattan distance from origin to
    the closest in the set of coordinates.
    """
    current_minimum = sys.maxsize

    for x, y in coordinates:
        if abs(x) + abs(y) < current_minimum:
            current_minimum = abs(x) + abs(y)

    return current_minimum

def shortest_combined_wire_path(grid):
    """
    Returns the distance value of the closest intersection by
    the length of the wire's paths.

    The return value is the addition of the two wires' total distances.
    """
    current_minimum = sys.maxsize

    for crossing in grid.crossings:
        crossing_wires = grid.get(crossing[0], crossing[1])
        
        crossing_total = 0
        for wire in crossing_wires:
            crossing_total += wire['distance']

        if crossing_total < current_minimum:
            current_minimum = crossing_total

        print(f"Total length of wire at {crossing} is {crossing_total}")
    return current_minimum

if __name__ == '__main__':
    main()
