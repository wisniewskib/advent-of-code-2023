from math import gcd
steps,_, *map = open("./inputs/day8.txt").read().splitlines()

instructions = {}

for x in map:
    position,destinations = x.split(" = ")
    instructions[position]=destinations[1:-1].split(", ")


count = 0

current="AAA"

while current!= "ZZZ":
    count+=1
    current = instructions[current][0 if steps[0]=="L" else 1]
    steps = steps[1:]+steps[0]

positions = [key for key in instructions if key.endswith("A")]
cycles=[]

for current in positions:
    cycle=[]

    current_steps = steps
    step_count = 0
    first_z = None

    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            current = instructions[current][0 if current_steps[0]=="L" else 1]
            current_steps = current_steps[1:]+current_steps[0]
            
        cycle.append(step_count)

        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break
        
    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm,num)

print(lcm)