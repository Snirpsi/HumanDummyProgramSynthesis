#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and stores user input. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        if number == -1:
            break
    print('The numbers are: ')
    for number in numbers:
        print(number)
    print('Thank you for using the 