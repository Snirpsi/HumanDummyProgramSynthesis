#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), UserInputHandler)
    
    server.serve_forever()
    
