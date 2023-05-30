#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    web = WebServer()
    web.serve_forever()
    
