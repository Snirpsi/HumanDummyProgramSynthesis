#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and prints user input. """    
    
    httpd = HTTPServer(('', 80), Fruit)
    httpd.serve_forever()
    
