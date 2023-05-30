#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        if number == '':
            break
        else:
            numbers.append(int(number))
    
    print('The numbers 