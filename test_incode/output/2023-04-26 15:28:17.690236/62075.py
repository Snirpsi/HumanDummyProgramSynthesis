#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and opens words. """    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
            
    words.sort()
    
    word