#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and opens a list of numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    httpd = HTTPServer(('', port), NumbersHandler)
    httpd.serve_forever()
    
