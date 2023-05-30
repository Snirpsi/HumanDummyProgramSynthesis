#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    for index, num in enumerate(numbers):
        print(index, num)
        #A conditional statement that checks if the index is greater than the length of the list.
        if index > len(numbers):
            break

