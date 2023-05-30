#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or removes a list of words. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, Handler)
    print('Serving on port ' + str(port))
    httpd.serve_forever()
    
