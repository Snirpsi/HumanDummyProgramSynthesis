#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and multiplyes a port. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()
