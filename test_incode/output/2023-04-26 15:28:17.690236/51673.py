#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and multiplyes a list of numbers. """    
    port = int(sys.argv[1])
    numbers = list(map(int, sys.argv[2:]))
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
