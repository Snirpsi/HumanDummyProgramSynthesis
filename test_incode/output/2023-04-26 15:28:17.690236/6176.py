#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and prints a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, WordsHandler)
    httpd.serve_forever()
    
