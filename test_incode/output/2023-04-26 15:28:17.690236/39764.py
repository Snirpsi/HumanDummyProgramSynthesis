#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()
