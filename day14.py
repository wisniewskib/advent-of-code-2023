def partOne():
    grid = open("./inputs/day14.txt").read().splitlines()
    grid = list(map("".join,zip(*grid)))
    sum=0
    for r, row in enumerate(grid):
        chunks = row.split("#")
        chunks = ["".join(sorted(chunk,reverse=True)) for chunk in chunks]
        grid[r] = "#".join(chunks)
        for c, char in enumerate(grid[r]):
            if char == "O":
                sum += len(row)-c
    print(sum)




def cycle(grid):
    grid = grid.splitlines();
    grid = list(map("".join,zip(*grid)))
    for r, row in enumerate(grid):
        chunks = row.split("#")
        chunks = ["".join(sorted(chunk,reverse=True)) for chunk in chunks]
        grid[r] = "#".join(chunks)
    grid = list(map("".join,zip(*grid)))
    for r, row in enumerate(grid):
        chunks = row.split("#")
        chunks = ["".join(sorted(chunk, reverse=True)) for chunk in chunks]
        grid[r] = "#".join(chunks)
    grid = list(map("".join,zip(*grid)))
    for r, row in enumerate(grid):
        chunks = row.split("#")
        chunks = ["".join(sorted(chunk)) for chunk in chunks]
        grid[r] = "#".join(chunks)
    grid = list(map("".join,zip(*grid)))
    for r, row in enumerate(grid):
        chunks = row.split("#")
        chunks = ["".join(sorted(chunk,)) for chunk in chunks]
        grid[r] = "#".join(chunks)
    return "\n".join(grid)
    


def partTwo():
    grid = open("./inputs/day14.txt").read()
    count=0
    seenGrids=set(grid)
    grids=[grid]
    while True:
        count+=1
        grid = cycle(grid)
        if grid in seenGrids:
            break
        grids.append(grid)
        seenGrids.add(grid)

    first = grids.index(grid)
    grid = grids[(1000000000 - first) % (count-first) + first]

    print(count, first)
    print(grid)
    print(sum(row.count("O") * (len(grid)-r) for r, row in enumerate(grid)))
    
    

partTwo()