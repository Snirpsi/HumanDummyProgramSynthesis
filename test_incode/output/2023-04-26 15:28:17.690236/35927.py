#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or removes all ports. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()
    
