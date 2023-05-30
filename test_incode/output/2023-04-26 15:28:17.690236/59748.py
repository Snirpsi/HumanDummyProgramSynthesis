#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    
    words = []
    
    with open('words.txt', 'r') as wordFile:
        for line in wordFile:
            words.append(line.strip())
    
    words.sort()
    
    for word in words:
        print(word)
    
