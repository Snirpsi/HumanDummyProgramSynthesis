#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or returns a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in ports:
            print(ports[word])
        else:
            print("Port not found")
    else:
        print("Usage: python3 add_word.py word")
    
    
