#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or adds fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    
    print('Serving at port %s' % port)
    
    httpd.serve_forever()
    
