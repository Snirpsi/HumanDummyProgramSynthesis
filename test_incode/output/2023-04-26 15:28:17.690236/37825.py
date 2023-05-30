#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or multiplyes fruits. """    
    ports = range(1,51)
    fruits = ['apple', 'banana', 'cherry']
    
    for port in ports:
        httpd = HTTPServer(('', port), MultiplyFruitHandler)
        httpd.serve_forever()
        
