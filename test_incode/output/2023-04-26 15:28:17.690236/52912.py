#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or removes a port. """    
    
    # Start the webserver
    httpd = HTTPServer(('', 8080), FruitHandler)
    print('Serving at http://127.0.0.1:8080/')
    httpd.serve_forever()
