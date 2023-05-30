#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and converts user input. """    
    
    while True:
        
        line = input('Enter a number: ')
        
        try:
            number = float(line)
        except ValueError:
            print('That is not a number!')
        else:
            print('The number you entered is', number)
            
