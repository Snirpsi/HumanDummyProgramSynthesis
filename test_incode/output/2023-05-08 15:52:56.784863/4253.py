#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that enumerates a list of numbers.
    for index, number in enumerate(numbers):
        print(index, number)
        #A conditional statement that checks if the index is greater than or equal to 3.
        if index > 3:
            break
        #A conditional statement that checks if the index is less than or equal to 9.
        if index < 9:
            break

