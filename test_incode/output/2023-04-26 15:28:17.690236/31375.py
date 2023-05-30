#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or opens words. """    
    
    while True:
        line = input('> ')
        if line == 'quit':
            break
        else:
            print(line)
    
