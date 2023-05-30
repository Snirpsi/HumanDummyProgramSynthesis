#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and opens words. """    
    
    import sys
    
    port = sys.argv[1]
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print("Serving on port 