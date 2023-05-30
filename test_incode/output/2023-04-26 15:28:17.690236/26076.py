#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and opens numbers. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving on port 