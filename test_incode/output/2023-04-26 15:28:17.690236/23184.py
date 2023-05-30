#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and returns words. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
    
