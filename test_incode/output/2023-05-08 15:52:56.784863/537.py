#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    for index, number in enumerate(numbers):
        print(index, number)
        #A break that stops the enumeration.
        if index == len(numbers)-1:
            break
        #A continue that continues the enumeration.
        else:
            continue

