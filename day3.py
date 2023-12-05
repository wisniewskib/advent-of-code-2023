import re
import sys

file = open("./inputs/day3.txt","r")
lines = file.readlines()

def partOne():
    sum=0
    for row in range(len(lines)):
        tempNumber=''
        isValid=False
        for column in range(len(lines[row])):
            current=lines[row][column]
            if(re.match(r'\d',current)):
                tempNumber+=current
                if(not isValid and isValidPart(row, column)):
                    isValid=True
            else:
                if isValid:
                    sum+=int(tempNumber)
                tempNumber=''
                isValid=False
    print(sum)

def partTwo():
    sum=0
    numbers = {}
    for row in range(len(lines)):
        tempNumber=''
        position=None
        for column in range(len(lines[row])):
            current=lines[row][column]
            if(re.match(r'\d',current)):
                tempNumber+=current
                if(not position ):
                    position=isGear(row, column)
            else:
                if position:
                    key=f"{position[0]},{position[1]}"
                    if key in numbers:
                        numbers[key].append(int(tempNumber))
                    else:
                        numbers[key]=[int(tempNumber)]
                tempNumber=''
                position=None
    for gears in numbers.values():
        if len(gears)==2:
            sum+=gears[0]*gears[1]
    print(sum)


def isValidPart(row, column):
    num_rows = len(lines)

    num_columns = len(lines[0])  

    cellsToCheck = [
        lines[row-1][column-1] if row > 0 and column > 0 else None,
        lines[row-1][column] if row > 0 else None,
        lines[row-1][column+1] if row > 0 and column < num_columns - 1 else None,
        lines[row][column-1] if column > 0 else None,
        lines[row][column+1] if column < num_columns - 1 else None,
        lines[row+1][column-1] if row < num_rows - 1 and column > 0 else None,
        lines[row+1][column] if row < num_rows - 1 else None,
        lines[row+1][column+1] if row < num_rows - 1 and column < num_columns - 1 else None
    ]
    for cell in cellsToCheck:        
        if cell and (re.match(r'[^0-9.\n]',cell)):
            return True
    return False

def isGear(row,column):
    num_rows = len(lines)
    num_columns = len(lines[0])  

    if row > 0 and column > 0 and lines[row-1][column-1] == "*":
        return [row-1, column-1]
    if row > 0 and lines[row-1][column] == "*":
        return [row-1, column]
    if row > 0 and column < num_columns - 1 and lines[row-1][column+1] == "*":
        return [row-1, column+1]
    if column > 0 and lines[row][column-1] == "*":
        return [row, column-1]
    if column < num_columns - 1 and lines[row][column+1] == "*":
        return [row, column+1]
    if row < num_rows - 1 and column > 0 and lines[row+1][column-1] == "*":
        return [row+1, column-1]
    if row < num_rows - 1 and lines[row+1][column] == "*":
        return [row+1, column]
    if row < num_rows - 1 and column < num_columns - 1 and lines[row+1][column+1] == "*":
        return [row+1, column+1]

    # If none of the conditions are met
    return False

partTwo()