#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = make_server('', port, httpd_handler)
    httpd.serve_forever()
    
