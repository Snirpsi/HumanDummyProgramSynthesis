#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or prints a port. """    
    import sys
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 80
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
