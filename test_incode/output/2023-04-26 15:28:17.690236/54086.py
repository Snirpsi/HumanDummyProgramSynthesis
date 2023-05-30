#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and adds user input. """    
    while True:
        line = input('Enter a number: ')
        print(line)
        
        if line == 'done':
            break
        else:
            