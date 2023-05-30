#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that enumerates numbers.
    #The program will ask the user to enter a number and then print
    #the number and the number of times it appears in the list.
    number = int(input('Enter a number: '))
    count = 0
    for number in numbers:
        if number == number:
            count += 1
    print('The number {} appears {} times.'.format(number, count))

