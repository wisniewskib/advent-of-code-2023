import re

times,distances = open("./inputs/day6.txt").read().split("\n")

times = list(map(int, times.split()[1:]))
distances = list(map(int,distances.split()[1:]))

def partOneAndTwo(times, distances):
    result = 1
    for race in range(0,len(times)):
        waysToBeat=0
        for i in range(0,times[race]):
            if(i*(times[race]-i)>distances[race]):
                waysToBeat+=1
        result*=waysToBeat
    print(result)

partOneAndTwo(times,distances)
partOneAndTwo([int(''.join(str(i) for i in times))],[int(''.join(str(i) for i in distances))])