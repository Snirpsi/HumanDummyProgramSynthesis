#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that returns a list of numbers.
    #The list will continue to grow as long as you keep adding numbers to the list.
    #The list will stop growing once you reach the number 9.
    numbers = []
    while len(numbers) < 9:
        numbers.append(int(input('Enter a number: ')))
    print(numbers)

