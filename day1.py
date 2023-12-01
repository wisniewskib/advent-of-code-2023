import re

file = open("./inputs/day1","r")
lines = file.readlines()

def partOne():
    sum = 0
    for line in lines:
        digits = re.findall("\d",line)
        sum += int(digits[0]+digits[len(digits)-1])
    print(sum)

def partTwo():
    numbers = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    sum = 0
    for line in lines:
        digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))',line)
        firstDigit =  digits[0] if digits[0].isdigit() else numbers[digits[0]]
        secondDigit = digits[len(digits)-1]
        secondDigit = secondDigit if secondDigit.isdigit() else numbers[secondDigit]
        print(line)
        print(digits)
        print(firstDigit+secondDigit)
        sum += int(firstDigit+secondDigit)
    print(sum)



# partOne()
partTwo()


