#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and returns a port. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
