# Jacobus Burger (2023)
# Advent of Code Day 3

def part1(filename):
    total = 0
    schematic = [line.strip() for line in open(filename).readlines()]
    queue = []  # remember digits in order
    width, height = len(schematic[0]), len(schematic)
    part = False
    print(f"width: {width}, height {height}, schematic: {schematic}")
    for i in range(width):
        for j in range(height):
            print(f"loop\nsymbol: {schematic[i][j]}, i: {i}, j: {j}")
            # we've reached the end of a sequence
            if schematic[i][j] == '.':
                print(f"  queue was {queue}, part {part}")
                # if we've reached the end of a valid part number
                if part:
                    # add the part number to the total
                    total += int(''.join(queue))
                    print(f"    total {total}")
                # reset queue and part flag
                part = False
                queue = []
            # add digits to queue in order (left-to-right)
            elif schematic[i][j].isdigit():
                print("  add digit to queue")
                queue.append(schematic[i][j])
            # look at all adjacent tiles (3x3 kernel) for part symbols
            for a in range(-1, 2):
                for b in range(-1, 2):
                    print("=== ab loop")
                    # bound pointers inside grid
                    x = max(0, min(9, i + a))
                    y = max(0, min(9, j + b))
                    print(f"(x{x}, y{y})")  # getting the wrong values
                    # check adjacent bounded tiles for any part symbols
                    symbol = schematic[y][x]
                    if not symbol.isdigit() and symbol != '.':
                        part = True
                    print(f"symbol: {symbol}, part {part}")
    return total