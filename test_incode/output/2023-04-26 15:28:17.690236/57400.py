#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'localhost'
        
    port = 8080
    
    webserver.serve(host, port, print_words)
    
