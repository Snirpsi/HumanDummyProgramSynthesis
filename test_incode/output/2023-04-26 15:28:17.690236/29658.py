#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.rstrip())
    
    words.sort()
    
    print('\n'.join(words))
    
