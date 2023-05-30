#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or adds user input. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, httpd)
    httpd.serve_forever()
    
