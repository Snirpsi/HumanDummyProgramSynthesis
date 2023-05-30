#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words. """    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
        
