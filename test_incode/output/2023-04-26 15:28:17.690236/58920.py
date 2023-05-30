#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or prints a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving on port ' + str(port) + '...')
    httpd.serve_forever()
    
