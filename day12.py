memo = {}

def count(cfg, nums):
    if (cfg,nums) in memo:
        return memo[(cfg,nums)]

    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0
    
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
        
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    memo[(cfg,nums)]=result

    return result


result=0
for line in open("./inputs/day12.txt").read().splitlines():
    springs, nums = line.split()

    springs = "?".join([springs]*5)
    nums=tuple(map(int,nums.split(",")))
    nums *= 5

    print(springs, nums)
    result+=count(springs,nums)

print(result)