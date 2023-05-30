#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()
    
