#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    
    print('Serving HTTP on port ' + str(port) + '...')
    httpd.serve_forever()
    
