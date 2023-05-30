#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or iterates over a list of numbers. """    
    port = int(sys.argv[1])
    numbers = sys.argv[2:]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    for number in numbers:
        server.