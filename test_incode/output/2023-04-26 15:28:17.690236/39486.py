#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or enumerates numbers. """    
    
    import sys
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Start server
    server = HTTPServer(("", 80), MyHandler)
    
    # Start server
    server.serve_forever()
    
