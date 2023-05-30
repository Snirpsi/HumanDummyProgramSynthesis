#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or stores a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    if port > 0:
        words.append("Port " + str(port))
    
    if port < 1024:
        words.append("Port " + str(port) + " 