from collections import deque

grid = open("./inputs/day16.txt").read().splitlines()


def determineDirection(y, x, d):
    tile = grid[y][x]
    newBeam = None
    if (tile == "/" and d == "R") or (tile == "\\" and d == "L"):
        d = "U"
    elif (tile == "\\" and d == "R") or (tile == "/" and d == "L"):
        d = "D"
    elif (tile == "/" and d == "U") or (tile == "\\" and d == "D"):
        d = "R"
    elif (tile == "\\" and d == "U") or (tile == "/" and d == "D"):
        d = "L"
    elif tile == "|" and (d == "R" or d == "L"):
        d = "U"
        newBeam = (y, x, "D")
    elif tile == "-" and (d == "D" or d == "U"):
        d = "L"
        newBeam = (y, x, "R")
    return d, newBeam


def energize(startingBeam=(0, -1, "R")):
    seenBeams = {startingBeam}
    beams = deque([startingBeam])
    energized = set()

    while beams:
        y, x, d = beams.popleft()

        if d == "R":
            x += 1
        elif d == "L":
            x -= 1
        elif d == "U":
            y -= 1
        elif d == "D":
            y += 1

        if x > len(grid[0]) - 1 or x < 0 or y < 0 or y > len(grid) - 1:
            continue

        if (y, x) not in energized:
            energized.add((y, x))

        newBeam = None
        d, newBeam = determineDirection(y, x, d)

        if newBeam and newBeam not in seenBeams:
            beams.append(newBeam)
            seenBeams.add(newBeam)

        if (y, x, d) not in seenBeams:
            seenBeams.add((y, x, d))
            beams.append((y, x, d))
    return len(energized)


# part 1
# print(energize())


def partTwo():
    topRow = [(-1, x, "D") for x in range(0, len(grid[0]))]
    bottomRow = [(len(grid), x, "U") for x in range(0, len(grid[0]))]
    leftColumn = [(y, -1, "R") for y in range(0, len(grid))]
    rightColumn = [(y, len(grid[0]), "L") for y in range(0, len(grid))]
    allConfigs = topRow + bottomRow + leftColumn + rightColumn
    allConfigs = map(energize, allConfigs)
    print(max(allConfigs))


partTwo()
