#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and calculates numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), NumberCalculator)
    server.serve_forever()
    
