#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or opens a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000
    
    httpd = make_server('', port, WordsHandler)
    httpd.serve_forever()
    
