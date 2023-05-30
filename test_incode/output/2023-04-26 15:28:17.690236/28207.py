#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or converts words. """    
    while True:
        line = input('> ')
        if line == 'quit':
            break
        elif line == 'quit\n':
            break
        else:
            print(line)
            
<|/ file ext=.py filename=