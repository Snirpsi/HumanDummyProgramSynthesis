#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and opens fruits. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()
    
    # 