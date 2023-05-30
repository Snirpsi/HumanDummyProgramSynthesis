#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    httpd = HTTPServer(('', 8080), FruitServer)
    httpd.serve_forever()
