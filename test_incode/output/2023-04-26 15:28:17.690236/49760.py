#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving at port", port)
    
    server.serve_forever()
    
