#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words. """    
    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    
    words.sort()
    
    for word in words:
        print(word)
    
