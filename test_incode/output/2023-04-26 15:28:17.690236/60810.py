#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or iterates over a port. """    
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
