#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and converts all ports. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), MyHandler)
    webserver.serve_forever()
    
