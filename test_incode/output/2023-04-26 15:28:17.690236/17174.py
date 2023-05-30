#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and adds a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(str(i))
    
    print("\n".join(words))
    
