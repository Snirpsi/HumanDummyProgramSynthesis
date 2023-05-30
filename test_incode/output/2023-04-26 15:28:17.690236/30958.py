#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'localhost'
    
    port = int(sys.argv[2])
    
    web = webserver.make_server(host, port)
    web.serve_forever()

<|/ file ext=.py |>