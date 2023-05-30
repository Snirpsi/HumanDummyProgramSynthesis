#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
