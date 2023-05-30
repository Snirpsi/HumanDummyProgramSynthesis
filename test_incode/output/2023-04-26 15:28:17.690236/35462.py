#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving at port", port)
    
    server.serve_forever()
    
