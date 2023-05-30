#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        words = []
        
        for i in range(port):
            words.append(raw_input())
            
        print(" ".join(words))
    else:
        print("Usage: python 