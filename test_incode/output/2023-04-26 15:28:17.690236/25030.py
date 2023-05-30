#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or adds a port. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('localhost', port, app)
    
    print('Serving at http://127.0.0.1:%s' % port)
    httpd.serve_forever()
    
