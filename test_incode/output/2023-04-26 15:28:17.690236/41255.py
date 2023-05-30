#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and removes words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for word in open(sys.argv[1]):
        if word.strip():
            words.append(word.strip())
    
    for word in words:
        word = word.strip()
        
        if word not in word