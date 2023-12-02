import re
import sys

file = open("./inputs/day2.txt","r")
lines = file.readlines()

red = 12
green = 13
blue = 14



def partOne():
    sum = 0
    for game in lines:
        gameId = re.search(r'Game (\d+):', game).group(1)
        print(gameId)
        setsInGame = game.split(':')[1].split(';')
        isValid = True
        for set in setsInGame:
            cubesInSet = re.findall(r'\d+\s\w+',set)
            for cube in cubesInSet:
                qty, color = cube.split(' ')
                qty = int(qty)
                if (color=='red' and qty >12 ) or (color=='green' and qty >13) or (color=='blue' and qty>14):
                    isValid=False
        if isValid:
            sum += int(gameId)
    print(sum)



def partTwo():
    sum = 0
    for game in lines:
        gameId = re.search(r'Game (\d+):', game).group(1)
        setsInGame = game.split(':')[1].split(';')
        minRed=0
        minGreen=0
        minBlue=0
        for set in setsInGame:
            cubesInSet = re.findall(r'\d+\s\w+',set)
            for cube in cubesInSet:
                qty, color = cube.split(' ')
                qty = int(qty)
                if color == 'red' and qty>minRed:
                    minRed = qty
                elif color == 'green' and qty>minGreen:
                    minGreen = qty
                elif color == 'blue' and qty>minBlue:
                    minBlue = qty
        power=minRed*minGreen*minBlue
        sum+=power
        print(sum)

partTwo()