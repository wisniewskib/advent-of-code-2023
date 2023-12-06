import re

file = open("./inputs/day4.txt","r")
lines = file.readlines()

def partOne():
    sum = 0
    colonIndex = lines[0].index(":")
    horizontalLineIndex = lines[0].index("|")
    for card in lines:
        winningNumbers = list(filter(None, card[colonIndex+1:horizontalLineIndex-1].split(" ")))
        cardNumbers = list(filter(None, card.replace("\n","")[horizontalLineIndex+1:len(card)].split(" ")))
        matches = list(set(winningNumbers) & set(cardNumbers))
        sum+=int(1*(2**(len(matches)-1)))
    print(sum)

def partTwo():
    colonIndex = lines[0].index(":")
    horizontalLineIndex = lines[0].index("|")
    cards=[1]*204
    for id, card in enumerate(lines):
        print(card)
        winningNumbers = list(filter(None, card[colonIndex+1:horizontalLineIndex-1].split(" ")))
        cardNumbers = list(filter(None, card.replace("\n","")[horizontalLineIndex+1:len(card)].split(" ")))
        matches = len(list(set(winningNumbers) & set(cardNumbers)))
        for i in range(matches):
            if len(cards) > id + i + 1:
                cards[id + i + 1] += cards[id]
    print(sum(cards))
        

partTwo()