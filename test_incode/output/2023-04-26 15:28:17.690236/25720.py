#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and adds user input. """    
    
    numbers = []
    
    while True:
        numbers.append(int(input('Enter a number: ')))
    
    print('The numbers entered are:')
    
    for number in numbers:
        print(number)
    
    print('\nThank you for playing!')
    
