import re

sequence = open("./inputs/day15.txt").read().split(",")


def hash(input):
    currentValue = 0
    for char in input:
        currentValue = (currentValue + ord(char)) * 17 % 256
    return currentValue


def partOne():
    sum = 0
    for step in sequence:
        sum += hash(step)
    print(sum)


# partOne()


def partTwo():
    boxes = [[] for i in range(0, 256)]
    for step in sequence:
        label, lens = re.split("=|-", step)
        boxNo = hash(label)

        if "=" in step:
            if any(label in currentLabel for currentLabel, x in boxes[boxNo]):
                for i, currentLens in enumerate(boxes[boxNo]):
                    if label in currentLens:
                        boxes[boxNo][i] = (label, lens)
                        break
            else:
                boxes[boxNo].append((label, lens))
        else:
            boxes[boxNo] = [
                currentLens for currentLens in boxes[boxNo] if label != currentLens[0]
            ]

    totalPower = 0
    for boxNumber, box in enumerate(boxes):
        for slotNumber, lens in enumerate(box):
            totalPower += (1 + boxNumber) * (1 + slotNumber) * int(lens[1])
    print(totalPower)


partTwo()
