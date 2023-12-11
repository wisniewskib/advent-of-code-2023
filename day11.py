grid = open("./inputs/day11.txt").read().splitlines()

emptyRows = [r for r,row in enumerate(grid) if "#" not in row]
emptyCols = [c for c,col in enumerate(zip(*grid)) if all(char == "." for char in col)]

points = [(r,c) for r,row in enumerate(grid) for c, char in enumerate(row) if char=="#"]

total=0
expansion=1000000

for i,(r1,c1) in enumerate(points):
    for (r2,c2) in points[:i]:
        for r in range(min(r1,r2),max(r1,r2)):
            total += 1 if r not in emptyRows else expansion
        for c in range(min(c1,c2),max(c1,c2)):
            total += 1 if c not in emptyCols else expansion

print(total)