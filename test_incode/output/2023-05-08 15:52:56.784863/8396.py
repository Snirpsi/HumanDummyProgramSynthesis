#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that requests numbers.
    while True:
        numbers.append(int(input('Enter a number: ')))
        #A conditional statement that checks if the user has entered a number.
        if numbers[-1] == int(input('Enter a number: ')): break
    print(numbers)

