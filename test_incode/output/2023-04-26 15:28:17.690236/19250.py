#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and stores a list of words. """    
    port = int(sys.argv[1])
    
    words = []
    
    for port in range(port, 65535):
        words.append(str(port))
    
    words.sort()
    
    for word in words:
        print(word)
    
    