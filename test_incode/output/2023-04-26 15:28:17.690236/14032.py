#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and multiplyes a port. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    port = int(sys.argv[1])
    
    for word in words:
        port = int(port) * int(word)
        
    print(port)
    
