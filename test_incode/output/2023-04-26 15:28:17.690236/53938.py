#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', port, FruitEnumerator)
    
    httpd.serve_forever()
    
