#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        line = input('> ')
        if line == 'quit':
            break
        else:
            print(line)
