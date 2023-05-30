#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    for index, number in enumerate(numbers):
        print(index, number)
    #A while loop that prints every number in the list until the end of the list.
    while index < len(numbers):
        print(numbers[index])
        index += 1

