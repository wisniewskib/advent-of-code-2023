workflows, parts = open("./inputs/day19.txt").read().split("\n\n")

workflows = {
    name: conditions.split(",")
    for name, conditions in (line[:-1].split("{") for line in workflows.splitlines())
}
parts = [
    {pair.split("=")[0]: int(pair.split("=")[1]) for pair in line[1:-1].split(",")}
    for line in parts.splitlines()
]


# print(parts)


def evaluateWorkflow(part, workflowId):
    workflow = workflows[workflowId]
    for stage in workflow:
        if ":" not in stage:
            return stage

        condition, target = stage.split(":")
        if ">" in condition:
            key, required = condition.split(">")
            if part[key] > int(required):
                return target
            else:
                continue
        elif "<" in condition:
            key, required = condition.split("<")
            if part[key] < int(required):
                return target
            else:
                continue


result = []
for part in parts:
    currentWorkflowId = evaluateWorkflow(part, "in")
    while True:
        if currentWorkflowId == "A":
            result.append(part)
            break
        elif currentWorkflowId == "R":
            break
        currentWorkflowId = evaluateWorkflow(part, currentWorkflowId)

# part1
# print(sum([sum(part.values()) for part in result]))

print(workflows)


def count(ranges, id="in"):
    if id == "R":
        return 0
    if id == "A":
        product = 1
        for low, hi in ranges.values():
            product *= hi - low + 1
        return product

    rules = workflows[id]
    fallback = rules[-1]

    total = 0

    for rule in rules[:-1]:
        key = rule[:1]
        operator = rule[1:2]
        required = int(rule.split(":")[0][2:])
        target = rule.split(":")[1]
        low, hi = ranges[key]
        if operator == "<":
            T = (low, required - 1)
            F = (required, hi)
        else:
            T = (required + 1, hi)
            F = (low, required)

        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)

    return total


print(count({key: (1, 4000) for key in "xmas"}))
