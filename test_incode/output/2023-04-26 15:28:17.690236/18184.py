#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and enumerates a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    # Print the list of words and enumerate the port
    for i in range(port):
        words.append(i)
        
    print(words)
    
    # Enumerate the port
    port = range(port)
    
    for port in port:
        print(port)
        
