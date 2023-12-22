import math
from collections import deque


class Module:
    def __init__(self, name, kind, outputs):
        self.name = name
        self.kind = kind
        self.outputs = outputs

        self.memory = {} if kind != "%" else "off"

    def __str__(self):
        return f"{self.name}{{type={self.kind},outputs={','.join(self.outputs)},memory={self.memory}}}"


modules = dict()
broadcast_targets = list()

with open("./inputs/day20.txt") as file:
    for line in file:
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outputs
        else:
            kind = left[0]
            name = left[1:]
            modules[name] = Module(name, kind, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].kind == "&":
            modules[output].memory[name] = "lo"

(feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

presses = 0

while True:
    presses += 1
    q = deque([("broadcaster", x, "lo") for x in broadcast_targets])

    while q:
        origin, target, pulse = q.popleft()

        if target not in modules:
            continue

        module = modules[target]

        if module.name == feed and pulse == "hi":
            seen[origin] += 1

            if origin not in cycle_lengths:
                cycle_lengths[origin] = presses
            else:
                assert presses == seen[origin] * cycle_lengths[origin]

            if all(seen.values()):
                lcm_val = 1
                for cycle_length in cycle_lengths.values():
                    lcm_val = lcm_val * cycle_length // math.gcd(lcm_val, cycle_length)
                print(lcm_val)
                exit()

        if module.kind == "%":
            if pulse == "lo":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "hi" if module.memory == "on" else "lo"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = (
                "lo" if all(value == "hi" for value in module.memory.values()) else "hi"
            )
            for x in module.outputs:
                q.append((module.name, x, outgoing))
