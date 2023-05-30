#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    for index, num in enumerate(numbers):
        print(index, num)
        #A conditional statement that prints out the number if index is even.
        if index % 2 == 0:
            print(num)

