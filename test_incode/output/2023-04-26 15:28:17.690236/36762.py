#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, Calculator)
    print('Serving on port %s' % port)
    httpd.serve_forever()
