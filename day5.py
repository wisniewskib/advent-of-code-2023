import re

def partTwo():
    inputs, *blocks = open("./inputs/day5.txt").read().split("\n\n")
    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds=[]
    for i in range(0,len(inputs), 2):
        seeds.append((inputs[i],inputs[i]+inputs[i+1]))

    for block in blocks:
        ranges=[]
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        newSeeds = []
        while len(seeds) > 0:
            s,e = seeds.pop()
            for a,b,c, in ranges:
                 os = max(s,b)
                 oe = min(e,b+c)
                 if os < oe:
                    newSeeds.append((os-b+a,oe-b+a))
                    if os > s:
                        seeds.append((s,os))
                    if e > oe:
                        seeds.append((oe,e))
                    break
            else:
                newSeeds.append((s,e))
        seeds = newSeeds
    print(sorted(seeds))

partTwo()




def partOne():
    seeds, *blocks = open("./inputs/day5.txt").read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges=[]
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        newSeeds = []
        for seed in seeds:
            for a,b,c in ranges:
                if b <= seed < b+c:
                    newSeeds.append(seed - b + a)
                    break
            else:
                newSeeds.append(seed  )                
        seeds = newSeeds

    print(min)