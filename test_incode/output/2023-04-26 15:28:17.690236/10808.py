#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    words = []
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    words.sort()
    
    for word in words:
        print(word)
        
