#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    for index, number in enumerate(numbers):
        print(index, number)
        #A conditional statement that checks if the index is greater than the length of the list.
        if index > len(numbers):
            break
        #A conditional statement that checks if the index is less than the length of the list.
        if index < 0:
            break

