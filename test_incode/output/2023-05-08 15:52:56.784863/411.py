#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    #The loop will stop when the number 9 is reached.
    for number in numbers:
        print(number)
        if number == 9:
            break
    #A break is used to exit the loop.

