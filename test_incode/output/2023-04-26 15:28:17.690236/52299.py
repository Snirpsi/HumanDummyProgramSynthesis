#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    
    words = []
    
    with open('words.txt', 'r') as wordFile:
        words = wordFile.read().splitlines()
        
    for word in words:
        print(word)
        
