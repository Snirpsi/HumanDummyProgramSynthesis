#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and multiplyes a list of words. """    
    port = int(sys.argv[1])
    words = [x.strip() for x in sys.argv[2:]]
    
    httpd = HTTPServer(('', port), Multiply