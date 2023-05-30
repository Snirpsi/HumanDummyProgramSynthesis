#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and opens user input. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('localhost', port, Handler)
    httpd.serve_forever()
    
