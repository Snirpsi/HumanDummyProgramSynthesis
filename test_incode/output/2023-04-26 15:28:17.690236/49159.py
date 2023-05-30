#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or opens words. """    
    
    import sys
    
    webserver_address = sys.argv[1]
    
    webserver = HTTPServer(webserver_address, FruitHandler)
    webserver.serve_forever()
    
