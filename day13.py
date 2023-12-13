grids = open("./inputs/day13.txt").read().split("\n\n")



def count(rows):
    for i in range(1,len(rows)):
        above = rows[0:i][::-1]
        below = rows[i:len(rows)]
        
        above = above[:len(below)]
        below = below[:len(above)]

        # part1
        # if above == below:
        # part2
        if sum(sum(1 if char1!=char2 else 0 for char1,char2 in zip(str1,str2)) for str1,str2 in zip(above,below))==1:
            return i
    return 0


total=0
for grid in grids:
    rows = grid.splitlines()
    columns = ["".join(column) for column in list(zip(*rows))]
    total+=count(rows)*100
    total+=count(columns)

print(total)