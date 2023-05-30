#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and multiplyes all ports. """    
    ports = [80, 8080, 443]
    
    for port in ports:
        httpd = HTTPServer(('', port), FruitHandler)
        httpd.serve_forever()
    
