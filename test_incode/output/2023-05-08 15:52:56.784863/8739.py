#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    #The list will never be empty
    while True:
        numbers.pop()
        print(numbers)
        if numbers == []:
            break

