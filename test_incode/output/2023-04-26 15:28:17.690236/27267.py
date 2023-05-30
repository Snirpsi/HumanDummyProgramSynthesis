#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and opens fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
