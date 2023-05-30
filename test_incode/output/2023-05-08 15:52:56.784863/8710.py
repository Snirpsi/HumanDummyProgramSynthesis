#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that requests a list of numbers.
    #The function will print them out in reverse order.
    print(numbers)
    print(numbers[::-1])
    print(numbers[::-1] + numbers)
    print(numbers[::-1] + numbers + numbers)

