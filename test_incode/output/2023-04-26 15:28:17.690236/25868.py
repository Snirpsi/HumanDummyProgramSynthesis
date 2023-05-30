#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, HelloHandler)
    httpd.serve_forever()
    
