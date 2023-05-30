#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and adds all ports. """    
    import sys
    from wsgiref.simple_server import make_server
    
    port = sys.argv[1]
    
    httpd = make_server('localhost', port, WordsApp)
    
    httpd.serve_forever()
    
