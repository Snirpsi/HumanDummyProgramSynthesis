#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and converts all ports. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    