#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and returns user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), MyHandler)
    webserver.serve_forever()
