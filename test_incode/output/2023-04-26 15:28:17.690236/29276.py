#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or opens a list of words. """    
    
    port = int(sys.argv[1])
    
    if port == 80:
        words = ['hello', 'world']
        
    elif port == 443:
        words = ['hello', 'world', 'how', 'are', 'you']
        
    elif port == 8080:
        words = ['hello', 'world', 'how', 'are', 'you', '