#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            
            if len(line) > 0:
                words.append(line)
                
    words.sort()
    
    for word in words:
        print(word)
        
