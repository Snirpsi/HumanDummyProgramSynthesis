#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words or returns a port. """    
    import sys
    
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
        
        words = []
        for i in range(port):
            words.append(str(i))
        
        print(" ".join(words))
    else:
        print("Usage: python3 wordlist.py <port>")
        
