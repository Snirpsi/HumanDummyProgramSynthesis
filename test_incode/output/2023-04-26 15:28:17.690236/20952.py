#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and multiplyes a port. """    
    
    import sys
    
    words = []
    port = int(sys.argv[1])
    
    for word in sys.argv[2:]:
        words.append(word)
    
    words.sort()
    
    for word in words:
        
        port = int(port)
        
        port = int(port*int(word))
        
        print('