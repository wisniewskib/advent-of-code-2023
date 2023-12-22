steps = open("./inputs/day18.txt").read().splitlines()


def partOne():
    trench = [(0, 0)]
    points = 0

    for step in steps:
        d, s, c = step.split()
        c = c[1:-1]

        s = int(s)
        points += s
        y, x = trench[-1]
        if d == "U":
            y -= s
        if d == "D":
            y += s
        if d == "L":
            x -= s
        if d == "R":
            x += s
        trench.append((y, x))

    area = (
        abs(
            sum(
                trench[i][0] * (trench[i - 1][1] - trench[(i + 1) % len(trench)][1])
                for i in range(len(trench))
            )
        )
        // 2
    )
    inside = area - points // 2 + 1

    print(inside + points)


def partTwo():
    trench = [(0, 0)]
    points = 0

    for step in steps:
        c = step.split()[2]
        c = c[2:-1]

        s = int(c[:-1], 16)
        d = int(c[-1])
        points += s
        y, x = trench[-1]
        if d == 3:
            y -= s
        if d == 1:
            y += s
        if d == 2:
            x -= s
        if d == 0:
            x += s
        trench.append((y, x))

    area = (
        abs(
            sum(
                trench[i][0] * (trench[i - 1][1] - trench[(i + 1) % len(trench)][1])
                for i in range(len(trench))
            )
        )
        // 2
    )
    inside = area - points // 2 + 1

    print(inside + points)


partTwo()
