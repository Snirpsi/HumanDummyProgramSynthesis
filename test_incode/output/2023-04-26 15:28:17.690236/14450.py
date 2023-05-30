#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    from wsgiref.simple_server import make_server
    
    server_address = ('', 8080)
    httpd = make_server(*server_address, WordsApp)
    
    httpd.serve_forever()
    
