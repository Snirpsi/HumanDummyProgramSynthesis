#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving HTTP on port 