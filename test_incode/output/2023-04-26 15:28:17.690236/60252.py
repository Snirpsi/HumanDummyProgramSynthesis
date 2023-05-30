#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    
    words = []
    with open('words.txt', 'r') as words:
        for line in words:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
        
