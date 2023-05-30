#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and multiplyes numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    