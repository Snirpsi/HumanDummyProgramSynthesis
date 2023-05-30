#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that prints a list of numbers.
    #The program will exit when the user enters a number that is
    #not in the list.
    while True:
        try:
            number = int(input('Enter a number: '))
            if number in numbers:
                print('The number you entered is in the list')
            else:
                print('The number you entered is not in the list')
        except ValueError:
            print('Invalid input')
        else:
            break

