#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or returns a list of words. """    
    while True:
        line = input()
        if line == 'exit':
            break
        else:
            print(line)
            
