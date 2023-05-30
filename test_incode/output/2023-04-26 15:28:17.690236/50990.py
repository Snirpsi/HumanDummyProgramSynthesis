#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and prints words. """    
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        words.append(line)
        
        if len(words) == 