#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or removes fruits. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        httpd = HTTPServer(('', port), FruitHandler)
        httpd.serve_forever()
        
