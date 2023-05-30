#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    #The list will continue to grow as more numbers are added
    #to it.
    numbers = list(numbers)
    while numbers:
        print(numbers.pop())

