#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and converts words. """    
    
    # start a server
    httpd = HTTPServer(("", 80), Handler)
    httpd.serve_forever()
    
    # 