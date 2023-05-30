#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and opens words. """    
    while True:
        line = input('Enter a word: ')
        if line == 'q':
            break
        else:
            print(line)
            
