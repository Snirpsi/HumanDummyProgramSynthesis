#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    from wsgiref.simple_server import make_server
    
    server_address = ("", 80)
    
    httpd = make_server(*server_address, WordsEnumerator)
    
    httpd.serve_forever()
    
