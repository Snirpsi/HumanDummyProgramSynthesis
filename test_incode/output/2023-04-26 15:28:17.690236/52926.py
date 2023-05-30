#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and opens a list of numbers. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    httpd = HTTPServer(('', ports[0]), MyHandler)
    httpd.serve_forever()
    
