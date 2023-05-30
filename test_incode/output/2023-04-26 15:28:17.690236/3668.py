#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or returns a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            print('Goodbye!')
            break
        else:
            numbers.append(int(number))
    
    print('Numbers:', numbers)
    
