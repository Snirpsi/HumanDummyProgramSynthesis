#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python ports.py [words]")
        sys.exit()
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: python ports.py [words]")
        sys.exit()
    
    ports = ports_generator()
    
    for word in words:
        ports = ports_generator()
        
        if word in ports:
            print(word)
        else:
            print(word + " not found in ports")
    
