#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    words = []
    
    for i in range(port):
        words.append(i)
        
    words.sort()
    
    for word in words:
        print(word)
    
