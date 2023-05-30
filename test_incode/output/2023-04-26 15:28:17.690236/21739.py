#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    httpd = make_server('', port, WordsHandler)
    httpd.serve_forever()
    
