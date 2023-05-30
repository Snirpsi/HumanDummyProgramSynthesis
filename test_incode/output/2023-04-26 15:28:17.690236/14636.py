#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and adds user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port 