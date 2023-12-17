from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in open("./inputs/day17.txt")]

seen = set()

queue = [(0, 0, 0, "", 0)]


def goInDirection(y, x, d):
    if d == "L":
        x -= 1
    elif d == "R":
        x += 1
    elif d == "D":
        y += 1
    elif d == "U":
        y -= 1
    return y, x


def isValidDirection(direction, d):
    return (
        d == "L"
        and direction != "R"
        or (d == "R" and direction != "L")
        or (d == "D" and direction != "U")
        or (d == "U" and direction != "D")
        or d == ""
    )


while queue:
    loss, y, x, d, c = heappop(queue)

    if y == len(grid) - 1 and x == len(grid[0]) - 1 and c >= 4:
        print(loss)
        break

    if (y, x, d, c) in seen:
        continue

    seen.add((y, x, d, c))

    if c < 10 and d != "":
        ny, nx = goInDirection(y, x, d)
        if nx < len(grid[0]) and ny < len(grid) and nx >= 0 and ny >= 0:
            heappush(queue, (loss + grid[ny][nx], ny, nx, d, c + 1))

    if c >= 4 or d == "":
        for direction in ["L", "R", "D", "U"]:
            if direction != d:
                if isValidDirection(direction, d):
                    ny, nx = goInDirection(y, x, direction)
                    if nx < len(grid[0]) and ny < len(grid) and nx >= 0 and ny >= 0:
                        heappush(queue, (loss + grid[ny][nx], ny, nx, direction, 1))
