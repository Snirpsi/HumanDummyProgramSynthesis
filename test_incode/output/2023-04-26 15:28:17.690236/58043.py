#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and returns a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    httpd = HTTPServer(('', port), NumbersHandler)
    httpd.serve_forever()
    
    print('Serving on port %s' % port)
    
