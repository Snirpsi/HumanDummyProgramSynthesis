#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words. """    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    for word in words:
        print(word)
        
