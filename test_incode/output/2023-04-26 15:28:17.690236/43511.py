#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or prints a list of numbers. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        number = int(input('Enter a number: '))
        if number == -1:
            break
        
        if number in words:
            print(number)
        else:
            print('Not a valid number')
    
