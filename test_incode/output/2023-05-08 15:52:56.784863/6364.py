#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    for index, number in enumerate(numbers):
        print(index, number)
        #A conditional statement that prints out the number if the index is even.
        if index % 2 == 0:
            print(number)
        #A conditional statement that prints out the number if the index is odd.
        if index % 2 != 0:
            print(number)
        #A conditional statement that prints out the number if the index is even.
        if index % 2 == 1:
            print(number)
        #A conditional statement that prints out the number if the index is odd.
        if index % 2 != 1:
            print(number)

