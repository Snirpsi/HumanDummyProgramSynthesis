#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or removes a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        httpd = make_server('', port, Handler)
        print('Serving on port %d ...' % port)
        httpd.serve_forever()
    else:
        print('Listen for port 0 ...')
        
