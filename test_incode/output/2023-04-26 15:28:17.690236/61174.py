#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        line = input('Enter a line to process: ')
        if line == 'q':
            break
        else:
            print(line)
