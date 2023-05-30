#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    words = []
    with open('words.txt') as file:
        for line in file:
            words.append(line.strip())
    
    words.sort()
    
    print(words)
    
