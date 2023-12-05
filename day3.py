import re
import sys

file = open("./inputs/day3.txt","r")
lines = file.readlines()

def partOne():
    sum=0
    for row in range(len(lines)):
        tempNumber='0'
        isValid=False
        for column in range(len(lines[row])):
            current=lines[row][column]
            if(re.match(r'\d',current)):
                tempNumber+=current
                if(isValidPart(row, column)):
                    isValid=True
            else:
                if isValid:
                    sum+=int(tempNumber)
                tempNumber='0'
                isValid=False
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
        if(re.match(r'[^0-9.]',cell)):
            return True
    return False

partOne()