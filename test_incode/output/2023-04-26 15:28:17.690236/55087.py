#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    words.sort()
    
    for word in words:
        print(word)
    
