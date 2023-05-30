#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RequestHandler)
    
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
    
