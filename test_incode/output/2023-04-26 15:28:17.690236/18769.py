#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and prints words. """    
    
    words = []
    
    for line in sys.stdin:
        words.append(line.strip())
    
    for word in words:
        print(word)
    
