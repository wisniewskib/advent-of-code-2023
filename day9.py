def extrapolate(array,backwards=False):
    if all(x==0 for x in array):
        return 0    
    diff=extrapolate([y-x for x,y in zip(array,array[1:])],backwards)
    return array[0]-diff if backwards else array[-1]+diff
total=0
for line in open("./inputs/day9.txt").read().splitlines():
    total+=extrapolate(list(map(int,line.split())),True)
print(total)